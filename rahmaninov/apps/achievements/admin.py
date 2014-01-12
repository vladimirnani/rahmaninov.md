from django.contrib import admin
from .models import (
    Olympiad,
    Laureate,
    Location,
    LaureateOlympiad,
    LaureateCompetition,
    Competition,
)

class LaureateCompetitionInline(admin.TabularInline):
    model = LaureateCompetition
    extra = 1


class LaureateOlympiadInline(admin.TabularInline):
    model = LaureateOlympiad
    extra = 1


class LaureateAdmin(admin.ModelAdmin):
    list_display = ('pupil', 'competitions_count',)
    inlines = [LaureateCompetitionInline, LaureateOlympiadInline]

    @staticmethod
    def competitions_count(obj):
        return obj.competitions.count()


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')


admin.site.register(Olympiad)
admin.site.register(Laureate, LaureateAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Location)
