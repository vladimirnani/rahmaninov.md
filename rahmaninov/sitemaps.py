from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from apps.achievements.models import Laureate
from apps.staff.models import Teacher


class TeacherSitemap(Sitemap):
    change_frequency = "never"

    def items(self):
        return Teacher.objects.all()

    def location(self, obj):
        return '/staff/' + str(obj.id)


class LaureateSitemap(Sitemap):
    change_frequency = "yearly"

    def items(self):
        return Laureate.objects.all()

    def location(self, obj):
        return '/achievements/laureates/{0}'.format(obj.pupil_id)


class StaticSitemap(Sitemap):
    def __init__(self, names, change_frequency):
        self.names = names
        self.change_frequency = change_frequency

    def items(self):
        return self.names

    def location(self, obj):
        return reverse(obj)

# SITEMAPS
SITEMAPS = {
    'static': StaticSitemap(
        [
            'index',
            'contacts',
            'admission',
            'history',
            'problem',
            'psycho',
            'library'
        ],
        'never'),
    'dynamic': StaticSitemap(
        [
            'laureates'
        ],
        'monthly'),
    'yearly': StaticSitemap(
        [
            'graduates',
            'staff',
            'olympiads',
            'barocco'
        ],
        'yearly'),
    'staff': TeacherSitemap,
    'laureates': LaureateSitemap,
}
