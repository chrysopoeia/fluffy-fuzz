import logging
import requests
import json
import re

from datetime import datetime

from django.core.management.base import BaseCommand
from ...models import WeatherForecast

logger = logging.getLogger('forecast')


class News24ForecastDecoder(json.JSONDecoder):
    def decode(self, json_string):
        json_string = json_string[:-3]    # strip contamination
        json_string = re.sub('new Date\(Date.UTC\((.+?)\)\)', '"\\1"', json_string) # format dates
        
        return super(News24ForecastDecoder, self).decode(json_string)


class Command(BaseCommand):
    help = "Fetches the weather forecast for the week from News24 for the given cities (77107 is Cape Town)"
    
    default_cities = [77107]
    
    def add_arguments(self, parser):
        parser.add_argument('city_id', nargs='*', type=int)
    
    def handle(self, *args, **kwargs):
        target_cities = kwargs.pop('city_id') or self.default_cities
        
        for target_city in target_cities:
            try:
                json_result = self.fetch_forecast(target_city)
                self.import_result(json_result)
            except Exception as e:
                logger.exception('Could not retrieve the weather for city: %s' % target_city)
    
    @classmethod
    def import_result(cls, json_result):
        """
        INSERT INTO forecast_weatherforecast(date, city, min_temp, max_temp, wind, rain) 
        VALUES (), ()
        ON CONFLICT ON CONSTRAINT
        DO UPDATE 
        min_temp=EXLUCDED.min_temp, 
        max_temp=EXLUCDED.max_temp,
        wind=EXLUCDED.wind,
        rain=EXLUCDED.rain
        """
        
        city = int(json_result['City'])
        
        for forecast in json_result.get('Forecasts'):
            min_temp = float(forecast['LowTemp'] or 0)
            max_temp = float(forecast['HighTemp'] or 0)
            wind = float(forecast['WindSpeed'] or 0)
            rain = float(forecast['Rainfall'] or 0)
            
            obj, created = WeatherForecast.objects.get_or_create(
                city=city,
                date=datetime(*map(int, forecast['Date'].split(','))),
                defaults=dict(
                    min_temp=min_temp,
                    max_temp=max_temp,
                    wind=wind,
                    rain=rain,
                )
            )
            
            if not created:
                obj.min_temp = min_temp
                obj.max_temp = max_temp
                obj.wind = wind
                obj.rain = rain
                obj.save()
    
    @classmethod
    def fetch_forecast(cls, target_city):
        response = requests.post(
            'http://weather.news24.com/ajaxpro/TwentyFour.Weather.Web.Ajax,App_Code.ashx',
            headers={
                'X-AjaxPro-Method': 'GetForecast7Day',
            }, 
            json={
                'cityId': str(target_city),
            })
        
        return response.json(cls=News24ForecastDecoder)
