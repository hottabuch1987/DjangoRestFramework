from django.contrib import admin
from .models import  User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone_number',  'last_login']
    list_filter = [ 'email', 'phone_number','gender']
    prepopulated_fields = {'email':('phone_number',)}
    date_hierarchy ='date_joined'
