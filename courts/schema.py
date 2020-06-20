import graphene
from graphene_django.types import DjangoObjectType
from bounce.courts.models import Court, Signup, MapStyle, MapAPIKey


class CourtType(DjangoObjectType):
    class Meta:
        model = Court

class SignupType(DjangoObjectType):
    class Meta:
        model = Signup

class MapStyleType(DjangoObjectType):
    class Meta:
        model = MapStyle

class MapAPIKeyType(DjangoObjectType):
    class Meta:
        model = MapAPIKey

class Query(object):
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