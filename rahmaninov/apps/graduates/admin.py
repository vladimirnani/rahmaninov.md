from django.contrib import admin
from .models import Graduate

class GraduateAdmin(admin.ModelAdmin):
    list_filter = ['year']
    search_fields = ['name']

admin.site.register(Graduate, GraduateAdmin)
