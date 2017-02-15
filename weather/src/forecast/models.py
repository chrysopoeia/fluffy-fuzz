from __future__ import unicode_literals

from django.db import models


class WeatherForecast(models.Model):
    date = models.DateField()
    city = models.IntegerField()
    
    min_temp = models.FloatField()
    max_temp = models.FloatField()
    wind = models.FloatField()
    rain = models.FloatField()
    
    def __unicode__(self):
        return "%(city)d " % ()
    
    class Meta:
        unique_together = ('date', 'city')
