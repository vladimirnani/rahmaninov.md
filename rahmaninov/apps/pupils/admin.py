from django.contrib import admin
from .models import Pupil, BaroccoMember


class PupilAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'teacher', 'subject')

admin.site.register(Pupil, PupilAdmin)
admin.site.register(BaroccoMember)
