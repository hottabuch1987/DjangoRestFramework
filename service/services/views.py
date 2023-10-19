from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Subscription, Service, Plan
from .serializers import SubscriptionSerializer, ServiceSerializer, PlanSerializer
from clients.models import User
from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class SubscriptionView(ReadOnlyModelViewSet):
    """subscriptions"""
    queryset = Subscription.objects.all().prefetch_related('plan', 'service',
        Prefetch('client', queryset=User.objects.all().only('phone_number', 'name')
    ))

    serializer_class = SubscriptionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id']
    search_fields = ['client__phone_number']
    ordering_fields = ['service__name']

#http://127.0.0.1:8000/api/v1/subscriptions/?id=3
#http://127.0.0.1:8000/api/v1/subscriptions/?search=89528792097
#http://127.0.0.1:8000/api/v1/subscriptions/?ordering=-service__name

class ServiceView(ReadOnlyModelViewSet):
    """service"""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class PlanView(ReadOnlyModelViewSet):
    """plan"""
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

