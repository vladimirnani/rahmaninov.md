from django.test import TestCase
from django.core.urlresolvers import reverse
from rahmaninov.sitemaps import StaticSitemap
from rahmaninov.urls import sitemaps


class StaticSitemapTests(TestCase):
    def setUp(self):
        names = [name for s in sitemaps.values()
                 if isinstance(s, StaticSitemap)
                 for name in s.names]
        self.urls = names

    def test_sitemap(self):
        """
        Every url should return HTTP_200_OK
        """
        for url in self.urls:
            response = self.client.get(reverse(url))
            self.assertEqual(response.status_code, 200)
