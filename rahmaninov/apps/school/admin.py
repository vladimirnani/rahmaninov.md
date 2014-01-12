from django.contrib import admin
from .models import Subject, Department

class SubjectAdmin(admin.ModelAdmin):
    list_filter = ('department',)

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Department)
