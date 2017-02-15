from __future__ import unicode_literals

from django.db import models

# Create your models here.

class WeatherForecast(models.Model):
    date = models.DateField()
    min_temp = models.IntegerField()
    max_temp = models.IntegerField()
    wind = models.IntegerField()
    rain = models.IntegerField()
