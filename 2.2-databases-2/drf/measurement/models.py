from django.db import models


class Sensor(models.Model):
    # id
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    changing_temp = models.IntegerField()
    changing_data = models.DateField(auto_now_add=True)
