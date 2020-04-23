from django.contrib.auth.models import User, Group
from .models import Court, MapStyle, MapAPIKey
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CourtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Court
        fields = ['id', 'name', 'road','city', 'state', 'county', 'country', 'likes', 'dislikes', 'location']

class MapStyleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapStyle
        fields = ['description', 'map_style']

class MapAPIKeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapAPIKey
        fields = ['api_key']