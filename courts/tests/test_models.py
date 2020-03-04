from django.test import TestCase
from courts.models import Court, MapAPIKey, MapStyle

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




