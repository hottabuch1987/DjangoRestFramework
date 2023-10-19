from .models import User
from rest_framework import serializers


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'phone_number')
