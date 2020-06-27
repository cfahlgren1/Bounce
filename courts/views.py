from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView
from .models import Court

# Create your views here.

longitude = -85.433690
latitude = 32.758153

user_location = Point(latitude, longitude, srid=4326)

class Home(generic.ListView):
    model = Court
    context_object_name = 'courts'
    queryset = Court.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:6]
    template_name = 'home/index.html'


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass

