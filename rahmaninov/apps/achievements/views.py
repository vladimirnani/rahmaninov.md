from jsonify.decorators import ajax_request
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.views.decorators.cache import cache_page
from .models import Laureate, LaureateCompetition, Location
import service


@cache_page(24 * 60 * 60)
def laureates(request):
    laureates = service.get_laureates()
    return render_to_response('laureates.html', RequestContext(request, locals()))


@cache_page(24 * 60 * 60)
def laureate(request, laureate_id):
    laureate = get_object_or_404(Laureate, pk=laureate_id)
    competitions = LaureateCompetition.objects.filter(laureate=laureate)
    return render_to_response('laureates-detail.html', RequestContext(request, locals()))


@cache_page(24 * 60 * 60)
def olympiads(request):
    laureates = service.get_olympiad_laureates()
    return render_to_response('olympiads.html', RequestContext(request, locals()))


@ajax_request
def locations(request):
    return {'locations': Location.objects.with_laureates()}


@cache_page(24 * 60 * 60)
def first_achievements(request):
    laureates = service.get_beginners()
    return render_to_response('first-steps.html', RequestContext(request, locals()))
