import graphene, graphql_geojson
from graphene_django.types import DjangoObjectType
from .models import Court, Signup, MapStyle, MapAPIKey


class CourtType(graphql_geojson.GeoJSONType):
    class Meta:
        model = Court
        geojson_field = 'location'


class SignupType(DjangoObjectType):
    class Meta:
        model = Signup


class MapStyleType(DjangoObjectType):
    class Meta:
        model = MapStyle


class MapAPIKeyType(DjangoObjectType):
    class Meta:
        model = MapAPIKey


class Query(graphene.ObjectType):
    all_courts = graphene.List(CourtType)
    all_map_styles = graphene.List(MapStyleType)
    all_map_api_key = graphene.List(MapAPIKeyType)
    all_signups = graphene.List(SignupType)

    def resolve_all_courts(self, info, **kwargs):
        return Court.objects.all()

    def resolve_all_map_styles(self, info, **kwargs):
        return MapStyle.objects.all()

    def resolve_all_map_api_key(self, info, **kwargs):
        return MapAPIKey.objects.all()

    def resolve_all_signups(self, info, **kwargs):
        return Signup.objects.all()
