from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from .models import Court

# Create your views here.

longitude = -82.782511
latitude = 30.600094

user_location = Point(latitude, longitude, srid=4326)

class Home(generic.ListView):
    model = Court
    context_object_name = 'courts'
    queryset = Court.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:6]
    template_name = 'home/index.html'

