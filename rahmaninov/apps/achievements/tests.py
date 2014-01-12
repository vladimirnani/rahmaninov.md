from django.test import TestCase
from .models import Location


class LocationsTest(TestCase):

    def test_locations(self):
        import pdb; pdb.set_trace()
        locations = Location.objects.with_laureates()
        print(locations)
        self.assertNotEqual(locations, None)
