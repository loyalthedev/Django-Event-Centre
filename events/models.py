from django.db import models


class Venue(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    capacity = models.IntegerField(default=500)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ('venue')
