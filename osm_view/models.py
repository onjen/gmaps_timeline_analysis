from __future__ import unicode_literals

from django.db import models


class Activity(models.Model):
    activity_type = models.CharField(max_length=20)
    confidence = models.IntegerField(default=0)

    def __str__(self):
        return self.activity_type


class Location(models.Model):
    timestamp = models.DateTimeField()
    lat = models.DecimalField(max_digits=8, decimal_places=6)
    lon = models.DecimalField(max_digits=8, decimal_places=6)
    accuracy = models.IntegerField(default=0)
    verticalAccuracy = models.IntegerField(default=0)
    activity = models.ManyToManyField(Activity)
    velocity = models.IntegerField(default=0)
    altitude = models.IntegerField(default=0)
    heading = models.IntegerField(default=0)

    def __str__(self):
        return "At {}, lat: {}, lon: {}".format(
                self.timestamp, self.lat, self.lon)
