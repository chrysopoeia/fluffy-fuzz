from rest_framework import serializers
from .models import WeatherForecast


class WeatherForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherForecast
        fields = ('city', 'date', 'min_temp', 'max_temp', 'wind', 'rain')
