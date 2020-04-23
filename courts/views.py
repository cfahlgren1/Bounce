from django.shortcuts import render
from .models import Court, MapStyle, MapAPIKey
from tablib import Dataset
from .resources import CourtResource
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.template import loader

from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, CourtSerializer, MapStyleSerializer, MapAPIKeySerializer



# list of mobile User Agents
mobile_uas = [
	'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
	'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
	'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
	'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
	'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
	'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
	'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
	'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
	'wapr','webc','winw','winw','xda','xda-'
	]

mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone' ]


def mobileBrowser(request):
    ''' Super simple device detection, returns True for mobile devices '''

    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]

    if (ua in mobile_uas):
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True

    return mobile_browser


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

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",

    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def detail(request):
    style = MapStyle.objects.get(active=True) # get map that is currently active
    mapbox_key = MapAPIKey.objects.get(active=True) # get first api_key; only should be one, can be changed later if rotating api keys etc.

    t = loader.get_template('courts/map/m_index.html')

    c = {'map_style': style,'api_key': mapbox_key.api_key,}  # page data
    return HttpResponse(t.render(c))

def handler500(request):
    return render(request, '500/index.html', status=500)


# API METHODS
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class MapStyleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MapStyle.objects.all()
    serializer_class = MapStyleSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CourtViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Court.objects.all().order_by('id')
    serializer_class = CourtSerializer

class MapAPIKeyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = MapAPIKey.objects.all()
    serializer_class = MapAPIKeySerializer