from .models import Subscription, Service, Plan
from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('__all__')


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('__all__')


class SubscriptionSerializer(serializers.ModelSerializer):
    client_phone = serializers.CharField(source='client.phone_number')
    client_name = serializers.CharField(source='client.name')
    plan = PlanSerializer()
    service = ServiceSerializer()

    class Meta:
        model = Subscription
        fields = ('id', 'client_phone', 'client_name', 'plan', 'service')
