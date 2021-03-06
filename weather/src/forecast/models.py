from __future__ import unicode_literals

from django.db import models


class WeatherForecast(models.Model):
    date = models.DateField()
    city = models.IntegerField()
    
    min_temp = models.FloatField()
    max_temp = models.FloatField()
    wind = models.FloatField()
    rain = models.FloatField()
    meta = models.TextField()
    
    def __unicode__(self):
        return "#%(city)d @ %(date)s %(min_temp)d-%(max_temp)d temp, %(wind)d wind, %(rain)d rain" % dict(
            city=self.city,
            date=self.date,
            min_temp=self.min_temp,
            max_temp=self.max_temp,
            wind=self.wind,
            rain=self.rain,
        )
    
    class Meta:
        unique_together = ('date', 'city')
