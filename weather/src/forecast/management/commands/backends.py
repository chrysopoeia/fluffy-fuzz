import requests
import re
import json

from datetime import datetime
from dateutil.relativedelta import relativedelta


class News24ForecastDecoder(json.JSONDecoder):
    DATE_REGEX = '(new Date\(Date.UTC\()(.+?)(\)\))'
    
    def __init__(self, *args, **kwargs):
        kwargs.update(object_hook=self.object_hook)
        super(News24ForecastDecoder, self).__init__(*args, **kwargs)
    
    def object_hook(self, obj):
        for k,v in obj.items():
            if re.match(self.DATE_REGEX, str(v)):
                # parse dates and add one month, JS months are 0-11
                v = re.sub(self.DATE_REGEX, '\\2', str(v))
                obj[k] = datetime(*map(int, v.split(','))) + relativedelta(months=1)
        
        return obj
    
    def decode(self, json_string):
        json_string = json_string[:-3]    # strip contamination
        json_string = re.sub(self.DATE_REGEX, '"\\1\\2\\3"', json_string) # format dates to string
        
        return super(News24ForecastDecoder, self).decode(json_string)


class News24Forecast(object):
    @staticmethod
    def fetch(target_city):
        return requests.post(
            'http://weather.news24.com/ajaxpro/TwentyFour.Weather.Web.Ajax,App_Code.ashx',
            headers={
                'X-AjaxPro-Method': 'GetForecast7Day',
            }, 
            json={
                'cityId': str(target_city),
            })
    
    @staticmethod
    def parse(response):
        json_result = response.json(cls=News24ForecastDecoder)
        parsed_results = []
        city = int(json_result['City'])
        
        for forecast in json_result.get('Forecasts'):
            defaults = {
                'min_temp': float(forecast['LowTemp'] or 0),
                'max_temp': float(forecast['HighTemp'] or 0),
                'wind': float(forecast['WindSpeed'] or 0),
                'rain': float(forecast['Rainfall'] or 0),
                'meta': response.text,
            }
            
            parsed_results.append({
                'date': forecast['Date'],
                'city': city,
                'defaults': defaults,
            })
        
        return parsed_results
