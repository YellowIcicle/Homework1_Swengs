from django.contrib import admin
from . import models


class CountryAdmin(admin.ModelAdmin):
    pass

    list_display = ['name']
    list_filter = ['name']
    sortable_by = ['name']
    search_fields = ['name']

admin.site.register(models.Country, CountryAdmin)

class ProducerAdmin(admin.ModelAdmin):
    pass

    list_display = ['name','founded','headquaters', "founder"]
    list_filter = ['name']

admin.site.register(models.Producer, ProducerAdmin)

class SmartphoneAdmin(admin.ModelAdmin):
    pass

    list_display = ['name','OS','release_date', "description", "price", "producer"]
    list_filter = ['name', 'OS', 'producer']
    sortable_by = ['name']

admin.site.register(models.Smartphone, SmartphoneAdmin)