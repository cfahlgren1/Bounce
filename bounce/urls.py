"""bounce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from .schema import schema
from courts import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'courts', views.CourtViewSet)
router.register(r'mapstyles', views.MapStyleViewSet)
router.register(r'api_keys', views.MapAPIKeyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),  # admin site
    path('', views.home, name="home"),  # home page
    path('courts/', views.detail, name="detail"),  # refer to court urls file
    path('api/', include(router.urls)),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('anomaly/', views.anomaly),
    path('robots.txt/', views.robots_txt), # add robots.txt link
    path ('loaderio-bfdc71f8924d72801af8766b33d8a6a4/', views.loaderio), # loaderio verification
]
handler500 = 'courts.views.handler500'