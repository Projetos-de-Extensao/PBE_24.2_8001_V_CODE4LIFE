from rest_framework import serializers
from .models import Convite

class ConviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convite
        fields = ['id', 'email']