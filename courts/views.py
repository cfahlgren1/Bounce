from django.shortcuts import render
from .models import Court, MapStyle, MapAPIKey
from tablib import Dataset
from .resources import CourtResource
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')

class MapStyleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MapStyle.objects.all()

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()

class CourtViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Court.objects.all().order_by('id')

def simple_upload(request):
    if request.method == 'POST':
        court_resource = CourtResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = court_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            court_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

def home(request):
    return render(request, 'courts/home/index.html')

def detail(request):
    style = MapStyle.objects.get(active=True) # get map that is currently active
    mapbox_key = MapAPIKey.objects.get(active=True) # get first api_key; only should be one, can be changed later if rotating api keys etc.

    return render(request, 'courts/map/index.html', {'map_style': style,'api_key': mapbox_key.api_key,})

def handler500(request):
    return render(request, '500/index.html', status=500)
