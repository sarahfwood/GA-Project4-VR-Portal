from rest_framework import serializers
from .models import Headset

class HeadsetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Headset
        fields = ('name', 'image', 'headset_type', 'connections', 'resolution', 'refresh_rate', 'motion_tracking', 'controls', 'hardware_platform', 'software_platform', 'description')