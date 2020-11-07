from django.shortcuts import render
from .models import Court, MapAPIKey, MapStyle
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.template import loader
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, CourtSerializer, MapStyleSerializer, MapAPIKeySerializer

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",

    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

# Error 500 page
def handler500(request):
    return render(request, '500/index.html', status=500)

# Error 404 page
def handler404(request, exception):
    return render(request, '404/index.html', status=404)


# API METHODS
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class MapStyleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MapStyle.objects.all()
    serializer_class = MapStyleSerializer


class ActiveMapStyleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MapStyle.objects.filter(active=True)  # get map that is currently active
    serializer_class = MapStyleSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CourtViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Court.objects.all()
    serializer_class = CourtSerializer


class MapAPIKeyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = MapAPIKey.objects.all()
    serializer_class = MapAPIKeySerializer

def anomaly(request):
    """
    Page to view anomaly / db statistical data
    """
    state_count = Court.objects.filter(state="unknown").count()
    country_count = Court.objects.filter(country="unknown").count()
    road_count = Court.objects.filter(road="unknown").count()
    total_basketball = Court.objects.filter(category="Basketball").count() # total courts
    total_tennis = Court.objects.filter(category="Tennis").count()  # total courts
    total_soccer = Court.objects.filter(category="Soccer").count()  # total courts
    total_users = User.objects.all().count() # total amount of users

    t = loader.get_template('anomaly/index.html')
    c = {'state_count': state_count, 'country_count': country_count, 'total_basketball': total_basketball, 'total_soccer': total_soccer, 'total_tennis': total_tennis, 'road_count': road_count, 'users_count': total_users}
    return HttpResponse(t.render(c))
