from django.contrib import admin
from .models import Store

# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'id', 'description')
    search_fields = ['name', 'description']
    list_filter = ['added']
    list_editable = ['description']


admin.site.register(Store, StoreAdmin)
