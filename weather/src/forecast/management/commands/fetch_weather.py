import logging
import requests
import json
import re

from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.core.management.base import BaseCommand
from ...models import WeatherForecast

logger = logging.getLogger('forecast')


class News24ForecastDecoder(json.JSONDecoder):
    def decode(self, json_string):
        json_string = json_string[:-3]    # strip contamination
        json_string = re.sub('new Date\(Date.UTC\((.+?)\)\)', '"\\1"', json_string) # format dates
        
        return super(News24ForecastDecoder, self).decode(json_string)


class News24Forecast(object):
    # map internal IDs to external ones
    CITY_MAP = {
        1: '77107',
    }
    
    @classmethod
    def fetch(cls, target_city):
        response = requests.post(
            'http://weather.news24.com/ajaxpro/TwentyFour.Weather.Web.Ajax,App_Code.ashx',
            headers={
                'X-AjaxPro-Method': 'GetForecast7Day',
            }, 
            json={
                'cityId': cls.CITY_MAP[target_city],
            })
        
        return response.json(cls=News24ForecastDecoder)
    
    @classmethod
    def parse(cls, json_result):
        parsed_results = []
        city = int(json_result['City'])
        
        for forecast in json_result.get('Forecasts'):
            defaults = {
                'min_temp': float(forecast['LowTemp'] or 0),
                'max_temp': float(forecast['HighTemp'] or 0),
                'wind': float(forecast['WindSpeed'] or 0),
                'rain': float(forecast['Rainfall'] or 0),
                'meta': json_result,
            }
            
            forecast_date = datetime(*map(int, forecast['Date'].split(','))) # parse date
            forecast_date += relativedelta(months=1)   # add one month, JS months are 0-11
            
            parsed_results.append(
                dict(defaults=defaults, date=forecast_date, city=city)
            )
        
        return parsed_results


class Command(BaseCommand):
    help = "Fetches the weather forecast for the week for the given cities (1 is Cape Town)"
    
    cities = {
        1: 'Cape Town',
    }
    
    default_cities = [1]
    default_backend = News24Forecast
    
    def add_arguments(self, parser):
        parser.add_argument('city_id', nargs='*', type=int)
        parser.add_argument('--cities', help='Print a list of usable cities', action='store_true')
        
    def list_cities(self):
        return str(self.cities)
    
    def handle(self, *args, **kwargs):
        if kwargs.pop('cities'):
            return self.list_cities()
        
        target_cities = kwargs.pop('city_id') or self.default_cities
        backend = self.default_backend
        
        for target_city in target_cities:
            try:
                raw_json_results = backend.fetch(target_city)
                logger.debug('results fetched %s' % str(raw_json_results))
                
                parsed_results = backend.parse(raw_json_results)
                logger.debug('results parsed %s' % str(parsed_results))
                
                for model_data in parsed_results:
                    obj, created = WeatherForecast.objects.update_or_create(**model_data)
                    logger.debug('results stored %d' % obj.pk)
                
            except Exception as e:
                logger.exception('Could not retrieve the weather for city: %s' % target_city)
        
        """
        PostgreSQL bulk:
        --~-~--~-~--~-~
        INSERT INTO forecast_weatherforecast(date, city, min_temp, max_temp, wind, rain)
        VALUES (), (), ()
        ON CONFLICT ON CONSTRAINT <forecast_weatherforecast_datecity_constraint_name>
        DO UPDATE 
        min_temp=EXLUCDED.min_temp, 
        max_temp=EXLUCDED.max_temp,
        wind=EXLUCDED.wind,
        rain=EXLUCDED.rain
        
        SQLite bulk:
        --~-~--~-~--~-~
        INSERT OR REPLACE INTO
        forecast_weatherforecast(date, city, min_temp, max_temp, wind, rain)
        VALUES (), (), ()
        """
