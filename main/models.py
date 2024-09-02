from django.db import models

class Temperature(models.Model):
    id = models.AutoField(primary_key=True)
    when = models.DateTimeField(null=True)
    sensor = models.CharField(null=True, max_length=32)
    value = models.IntegerField(null=True)
