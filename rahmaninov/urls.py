from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from rahmaninov.apps.pupils.models import BaroccoMember
from rahmaninov.apps.graduates.models import Graduate
from rahmaninov.sitemaps import SITEMAPS

ONE_DAY = 24 * 60 * 60

# Website
urlpatterns = patterns(
    'rahmaninov.apps.website.views',
    url(r'^$', 'index', name='index'),
    url(r'^info/psycho/$', TemplateView.as_view(template_name='articles/psycho.html'), name='psycho'),
    url(r'^info/library/$', TemplateView.as_view(template_name='articles/library.html'), name='library'),
    url(r'^info/reasons/$', TemplateView.as_view(template_name='articles/reasons.html'), name='reasons'),
    url(r'^info/admission/$', TemplateView.as_view(template_name='admission.html'), name='admission'),
    url(r'^contacts/$', TemplateView.as_view(template_name='contacts.html'), name='contacts'),
    url(r'^articles/history/$', TemplateView.as_view(template_name='history.html'), name='history'),
    url(r'^articles/problem/$', TemplateView.as_view(template_name='problem.html'), name='problem'),
    url(r'^achievements/barocco$', cache_page(ONE_DAY)(ListView.as_view(model=BaroccoMember, template_name='barocco.html')), name='barocco'),
    url(r'^robots.txt$', TemplateView.as_view(template_name='robots.txt'))
)

# Achievements
urlpatterns += patterns(
    'rahmaninov.apps.achievements.views',
    url(r'^achievements/olympiads$', 'olympiads', name='olympiads'),
    url(r'^achievements/laureates/$', 'laureates', name='laureates'),
    url(r'^achievements/locations/$', 'locations'),
    url(r'^achievements/laureates/(?P<laureate_id>\d+)/$', 'laureate', name='laureate'),
    url(r'^achievements/first_achievements/$', 'first_achievements', name='first_achievements'),
)

# Staff
urlpatterns += patterns(
    'rahmaninov.apps.staff.views',
    url(r'^staff/$', 'staff', name='staff'),
    url(r'^staff/(?P<teacher_id>\d+)/$', 'teacher', name='teacher'),
)

# Gallery
urlpatterns += patterns(
    'rahmaninov.apps.gallery.views',
    url(r'^gallery/(?P<set_id>\d+)/$', 'photoset', name='photoset'),
)

# Graduates
urlpatterns += patterns(
    'rahmaninov.apps.graduates.views',
    url(r'^graduates/$', cache_page(ONE_DAY)(ListView.as_view(model=Graduate, template_name='people/graduates.html')), name='graduates'),
)

# ADMIN
admin.autodiscover()
urlpatterns += patterns(
    '',
    url(r'^admin/', include(admin.site.urls))
)

urlpatterns += patterns(
    'django.contrib.sitemaps.views',
    url(r'^sitemap\.xml$', 'sitemap', {'sitemaps': SITEMAPS})
)

# STATIC FILES
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        url(r'^media/(?P<path>.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
