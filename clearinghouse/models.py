from django.db import models
try:
    from .PersonCourt import PersonCourt
except ImportError:
    pass

class Court(models.Model):
    name = models.CharField(max_length=240)
    ch_id = models.IntegerField()

class Person(models.Model):
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
