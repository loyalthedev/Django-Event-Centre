from django.db import models


class Venue(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    capacity = models.IntegerField(default=500)
