from rest_framework import serializers
from .models import Headset

class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ('model_type')

class HeadsetSerializer(serializers.ModelSerializer):

    headset_type = TypeSerializer()
    
    class Meta:
        model = Headset
        fields = ('name', 'image', 'headset_type', 'connections', 'resolution', 'refresh_rate', 'motion_tracking', 'controls', 'hardware_platform', 'software_platform', 'description')