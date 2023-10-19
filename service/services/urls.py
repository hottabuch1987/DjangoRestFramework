from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubscriptionView, PlanView, ServiceView


router = DefaultRouter()
router.register('subscriptions', SubscriptionView, basename='subscriptions')
router.register('service', ServiceView, basename='service')
router.register('plan', PlanView, basename='plan')


urlpatterns = [
    path('', include(router.urls)),    
]

