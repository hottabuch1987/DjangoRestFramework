from django.contrib import admin
from .models import Plan, Service, Subscription


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'full_price']
    list_filter = [ 'name', 'full_price']
    


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['plan_types', 'discount_percent']
    list_filter = [ 'plan_types', 'discount_percent']
    
    


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['client', 'service',  'plan']
    list_filter = [ 'client', 'service','plan']
    