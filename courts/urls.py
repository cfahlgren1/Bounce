from django.urls import include, path
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'courts'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # home page
    url(r'^$', views.detail, name='detail'),
]
urlpatterns += staticfiles_urlpatterns()