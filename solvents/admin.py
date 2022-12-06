
from django.contrib import admin
from .models import solvents
# Register your models here.
class SolevntsAdmin(admin.ModelAdmin):
    list_display = ['id','name','company','qty','price']
admin.site.register(solvents,SolevntsAdmin)