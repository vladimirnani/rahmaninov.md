from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page
from rahmaninov.apps.gallery.models import GalleryCollection
from rahmaninov.apps.events.models import Event
import rahmaninov.apps.gallery.views


@cache_page(60 * 60)
def index(request):
    events_list = Event.objects.all()
    collections = GalleryCollection.objects.all()
    rahmaninov.apps.gallery.views.update_collections(collections)
    return render_to_response('index.html', RequestContext(request, locals()))

