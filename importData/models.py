from django.db import models

import datetime

class ZipCode(models.Model):
    zipcode = models.CharField(max_length=5)
    city = models.CharField(max_length=64)
    statecode = models.CharField(max_length=2)
    statename = models.CharField(max_length=32)
    create_date = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return "%s, %s (%s)" % (self.city, self.statecode, self.zipcode)

    class Meta:
        ordering = ['zipcode']

    def __str__(self):
        return self.zipcode