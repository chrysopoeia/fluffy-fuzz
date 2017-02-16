import logging

from django.core.management.base import BaseCommand
from ...models import WeatherForecast
from .backends import News24Forecast

logger = logging.getLogger('forecast')


class Command(BaseCommand):
    help = "Fetches the weather forecast for the week for the given cities"
    
    default_city = 77107              # this exercise assumes city id's are generic across backends
    default_backend = News24Forecast
    
    def add_arguments(self, parser):
        parser.add_argument('city_id', nargs='?', type=int)
        
    def handle(self, *args, **kwargs):
        target_city = kwargs.pop('city_id') or self.default_city
        backend = self.default_backend    # could allow backend to be chosen via args
        
        try:
            response = backend.fetch(target_city)
            logger.debug('results fetched %s' % str(response.text))
            
            parsed_results = backend.parse(response)
            logger.debug('results parsed %s' % str(parsed_results))
            
            for model_data in parsed_results:
                obj, created = WeatherForecast.objects.update_or_create(**model_data) # could use SQL for a bulk upsert
                logger.info('results stored %s' % obj.date)
            
        except Exception as e:
            logger.exception('Could not retrieve the weather for city: %s' % target_city)
