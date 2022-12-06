from django.contrib import admin
from .models import inorganic
# Register your models here.
class InOrganicAdmin(admin.ModelAdmin):
    list_display = ['id','name','company','qty','price']
admin.site.register(inorganic,InOrganicAdmin)