from django.test import TransactionTestCase
from .models import WeatherForecast
from django.core.management import call_command

from datetime import datetime, timedelta


class ForecastTest(TransactionTestCase):
    
    def test_fetch_weather(self):
        now = datetime.now()
        
        self.assertEquals(WeatherForecast.objects.all().count(), 0)
        
        call_command('fetch_weather')
        
        test_results = WeatherForecast.objects.filter(
            date__gte=now, 
            date__lt=now + timedelta(days=7),
        )
        
        self.assertEquals(test_results.count(), 7)
