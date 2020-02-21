from django.db import models

# Create your models here.
class Headset(models.Model):
    name = models.CharField(max_length=50)
    headset_type = models.CharField(max_length=50)
    connections = models.CharField(max_length=50)
    resolution = models.CharField(max_length=50)
    refresh_rate = models.CharField(max_length=50)
    motion_tracking = models.CharField(max_length=50)
    controls = models.CharField(max_length=50)
    hardware_platform = models.CharField(max_length=50)
    software_platform = models.CharField(max_length=50)
