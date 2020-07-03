from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Court
import requests, json

# Create your views here.
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


def detail(request):
    """
    Courts Page
    """
    theArray = []

    for i in range(1,20):
        offset = 100 * i
        # api-endpoint
        URL = "https://bouncemap.com/api/courts/?format=json&offset=" + str(offset)

        PARAMS = {}
        r = requests.get(url=URL, params=PARAMS)

        # extracting data in json format
        data = r.json()

        # if len(data['results']) == 0:
        #    break
        theArray.append(json.dumps(data))
    t = loader.get_template('home/index.html')

    c = {'json_array': theArray}  # page data
    return HttpResponse(t.render(c))


