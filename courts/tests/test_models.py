from django.test import TestCase
from django.contrib.gis.geos import fromstr
from ..models import Court, MapAPIKey, MapStyle

class CourtTest(TestCase):

    def setUp(self):
        longitude = -80.191788
        latitude = 25.761681
        self.court = Court.objects.create(
            name="Frank Brown Rec Center",
            house_number=235,
            road="Opelika Road",
            city="Auburn",
            state="AL",
            country="United States",
            location=fromstr(f'POINT({longitude} {latitude})', srid=4326)
        )

    # Check to see if it was created and named correctly
    def test_court_is_named_correctly(self):
        self.assertEquals(self.court.__str__(), self.court.name + " " + self.court.description)

    # Make sure likes data can be modified
    def test_court_likes_increases(self):
        self.court.likes += 45
        self.court.save()
        self.assertEquals(self.court.likes, 45)

    # Make sure likes data can be modified
    def test_court_likes_decreases(self):
        self.court.likes = 31
        self.court.save()
        self.court.likes -= 1
        self.assertEquals(self.court.likes, 30)

    # Make sure likes data can be modified
    def test_court_name_change(self):
        self.court.name = "Other Test Name"
        self.court.save()
        self.assertEquals(self.court.__str__(), "Other Test Name "  + self.court.description)

    # Make sure likes data can be modified
    def test_court_address_change(self):
        self.court.address = "Harper Ave"
        self.court.save()
        self.assertEquals(self.court.address, "Harper Ave")

# MapStyle Tests
class MapStyleTest(TestCase):
    def create_map_style(self, mapstyle='testtesttest', description='onlyatestdescription'):
        return MapStyle.objects.create(map_style=mapstyle, description=description)

    def test_map_style_rep(self):
        w = self.create_map_style()
        self.assertTrue(isinstance(w, MapStyle))
        self.assertEqual(w.__str__(), w.description) # test model str representation

    def test_map_values(self):
        w = self.create_map_style()
        self.assertEqual(w.map_style, 'testtesttest') #test mapstyle code created above
        self.assertEqual(w.description, 'onlyatestdescription') #test description created above

#MapAPIKey Tests
class MapAPIKeyTest(TestCase):
    def create_api_key(self, key='testkeytestkey'):
        return MapAPIKey.objects.create(api_key=key)

    def test_map_api_rep(self):
        w = self.create_api_key()
        self.assertTrue(isinstance(w, MapAPIKey))
        self.assertEqual(w.__str__(), w.api_key)

    def test_map_values(self):
        w = self.create_api_key()
        self.assertEqual(w.api_key, 'testkeytestkey')


