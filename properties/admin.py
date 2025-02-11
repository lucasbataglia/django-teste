from django.contrib import admin
from properties.models import Propertie

# Register your models here.
class PropertieAdmin(admin.ModelAdmin):
    list_display= ('name','sellType', 'price', 'fullAddress')
    search_fields = ('name','sellType', 'price', 'fullAddress',)

admin.site.register(Propertie, PropertieAdmin)