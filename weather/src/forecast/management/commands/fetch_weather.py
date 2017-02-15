import requests
import json
import re

from django.core.management.base import BaseCommand
from ...models import WeatherForecast


class News24ForecastDecoder(json.JSONDecoder):
    def decode(self, json_string):
        json_string = json_string[:-3]    # strip contamination
        json_string = re.sub('"Date":(.+?)\),', '"Date": "\\1",', json_string) # coerce JS Date declarations to string
        
        return super(News24ForecastDecoder, self).decode(json_string)


class Command(BaseCommand):
    help = "Fetches the weather forecast for the week from News24 for the given cites (77107 is Cape Town)"
    
    def add_arguments(self, parser):
        parser.add_argument('city_id', nargs='+', type=int)
    
    def handle(self, *args, **kwargs):
        target_cities = kwargs.pop('city_id')
        
        for target_city in target_cities:
            self.fetch_forecast(str(target_city))
    
    def fetch_forecast(self, target_city):
        source_url = 'http://weather.news24.com/ajaxpro/TwentyFour.Weather.Web.Ajax,App_Code.ashx'
        
        headers = {
            'X-AjaxPro-Method': 'GetForecast7Day',
            'Content-Type': 'text/plain; charset=utf-8',
        }
        
        data = {
            'cityId': target_city,
        }
        
        response = requests.post(source_url, headers=headers, json=data)
        response.json(cls=News24ForecastDecoder)
