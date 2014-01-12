from datetime import date
from django.utils.datastructures import SortedDict
from .models import (
    Laureate,
    LaureateOlympiad,
    LaureateCompetition,
    Competition,
)

def find_beginners(laureates):
    BEGINNERS_POSITIONS = [0, 6]
    for laureate in laureates:
        for competition in laureate.laureatecompetition_set.all():
            if competition.position not in BEGINNERS_POSITIONS:
                laureate.is_beginner = False
                continue

def find_recent(laureates):
    this_year = date.today().year
    for laureate in laureates:
        for competition in laureate.laureatecompetition_set.all():
            if competition.year == this_year:
                laureate.this_year_laureate = True
                continue

def get_laureates():
    laureates = list(Laureate.objects.all())
    find_beginners(laureates)
    find_recent(laureates)
    laureates = [x for x in laureates if not x.is_beginner]
    return laureates


def get_beginners():
    laureates = list(Laureate.objects.all())
    find_beginners(laureates)
    find_recent(laureates)
    laureates = [x for x in laureates if x.is_beginner]
    return laureates


def get_olympiad_laureates():
    current_year = date.today().year
    result = SortedDict()

    laureate_olympiads = list(LaureateOlympiad.objects
                                              .all()
                                              .order_by('-year')
                                              .select_related())

    all_laureates = [x.laureate for x in laureate_olympiads]

    recent_olympiads = [x for x in laureate_olympiads if x.year == current_year]
    recent_laureates = []
    for laureate in all_laureates:
        for olympiad in recent_olympiads:
            if olympiad.laureate == laureate:
                recent_laureates.append(laureate)
    recent_laureates = set(recent_laureates)

    old_laureates = [x for x in all_laureates if x not in recent_laureates]

    laureates = list(recent_laureates) + list(old_laureates)

    for laureate in laureates:
        result[laureate.name] = [x for x in laureate_olympiads
                                 if x.laureate == laureate]

    return result
