from django.views.decorators.cache import cache_page
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
import flickr
from .models import GalleryCollection

def update_collections(collections):
    flickr.API_KEY = 'c1f877b4f6f168f6cc90d03e73ca47be'
    for collection in collections:
        if not collection.cover_photo:
            photoset = flickr.Photoset(collection.photoset_id)
            for photo in photoset.getPhotos():
                medium = photo.getSizes()[5]
                if medium['width'] == 500 and medium['height'] == 333:
                    collection.cover_photo = medium['source']
                    collection.save()
                    break


@cache_page(24 * 60 * 60)
def photoset(request, set_id):
    collection = get_object_or_404(GalleryCollection, pk=set_id)
    return render_to_response('photoset.html',
                              RequestContext(request, locals()))

