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
    all_basketball_courts = graphene.List(CourtType)
    all_map_styles = graphene.List(MapStyleType)
    all_map_api_key = graphene.List(MapAPIKeyType)
    all_signups = graphene.List(SignupType)

    # Return all basketball courts to endpoint
    def resolve_all_basketball_courts(self, info, **kwargs):
        return Court.objects.all().filter(category='Basketball')

    # Return all map styles to endpoint
    def resolve_all_map_styles(self, info, **kwargs):
        return MapStyle.objects.all()

    # Return all map api keys to endpoint
    def resolve_all_map_api_key(self, info, **kwargs):
        return MapAPIKey.objects.all()

    # Return all user signups to endpoint
    def resolve_all_signups(self, info, **kwargs):
        return Signup.objects.all()
