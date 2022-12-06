from django.contrib import admin
from .models import organic

# Register your models here.
class OrganicAdmin(admin.ModelAdmin):
    list_display = ['id','name','company','qty','price']
admin.site.register(organic,OrganicAdmin)