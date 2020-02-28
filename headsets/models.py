from django.db import models

# Create your models here.
class Type(models.Model):
    model_type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.model_type}'

class Headset(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    headset_type = models.ForeignKey(Type, related_name='headsets', on_delete=models.CASCADE)
    connections = models.CharField(max_length=50)
    resolution = models.CharField(max_length=50)
    refresh_rate = models.CharField(max_length=50)
    motion_tracking = models.CharField(max_length=50)
    controls = models.CharField(max_length=50)
    hardware_platform = models.CharField(max_length=50)
    software_platform = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name}'
