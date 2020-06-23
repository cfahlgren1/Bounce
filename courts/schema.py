import graphene, graphql_geojson
from django.db.models import Q
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
    all_basketball_courts = graphene.List(CourtType, id=graphene.ID(), name=graphene.String(), city=graphene.String(), state=graphene.String(), first=graphene.Int(), skip=graphene.Int())
    all_soccer_fields = graphene.List(CourtType, id=graphene.ID(), name=graphene.String(), city=graphene.String(), state=graphene.String(), first=graphene.Int(), skip=graphene.Int())
    all_tennis_courts = graphene.List(CourtType, id=graphene.ID(), name=graphene.String(), city=graphene.String(), state=graphene.String(), first=graphene.Int(), skip=graphene.Int())
    all_map_styles = graphene.List(MapStyleType, mapstyle=graphene.String(), first=graphene.Int(), skip=graphene.Int())
    all_map_api_key = graphene.List(MapAPIKeyType)
    all_signups = graphene.List(SignupType, first=graphene.Int(), skip=graphene.Int())

    # Return all basketball courts to endpoint
    def resolve_all_basketball_courts(self, info, id=None, name=None, city=None, state=None, first=None, skip=None, **kwargs):
        courts = Court.objects.filter(category="Basketball")

        # if id is given, return court with id, else none
        if id:
            return [Court.objects.get(pk=id)]

        # if name argument is given, return courts with name containing argument
        if name:
            filter = (
                Q(name__icontains=name)
            )
            courts = courts.filter(filter)

        # if city argument is given, return courts with name containing argument
        if city:
            filter = (
                Q(city__icontains=city)
            )
            courts = courts.filter(filter)

        # if state argument is given, return courts with name containing argument
        if state:
            filter = (
                Q(state__icontains=state)
            )
            courts = courts.filter(filter)

        # if skip is given, skip n values
        if skip:
            courts = courts[skip:]

        # if first is given, return only that many objects
        if first:
            courts = courts[:first]
        return courts

    # Return all tennis courts to endpoint
    def resolve_all_tennis_courts(self, info, id=None, name=None, city=None, state=None, first=None, skip=None, **kwargs):
        courts = Court.objects.filter(category="Tennis")

        # if id is given, return court with id, else none
        if id:
            return [Court.objects.get(pk=id)]

        # if name argument is given, return courts with name containing argument
        if name:
            filter = (
                Q(name__icontains=name)
            )
            courts = courts.filter(filter)

        # if city argument is given, return courts with name containing argument
        if city:
            filter = (
                Q(city__icontains=city)
            )
            courts = courts.filter(filter)

        # if state argument is given, return courts with name containing argument
        if state:
            filter = (
                Q(state__icontains=state)
            )
            courts = courts.filter(filter)

        # if skip is given, skip n values
        if skip:
            courts = courts[skip:]

        # if first is given, return only that many objects
        if first:
            courts = courts[:first]
        return courts

    # Return all soccer fields to endpoint
    def resolve_all_soccer_fields(self, info, id=None, name=None, city=None, state=None, first=None, skip=None, **kwargs):
        courts = Court.objects.filter(category="Soccer")

        # if id is given, return court with id, else none
        if id:
            return [Court.objects.get(pk=id)]

        # if name argument is given, return courts with name containing argument
        if name:
            filter = (
                Q(name__icontains=name)
            )
            courts = courts.filter(filter)

        # if city argument is given, return courts with name containing argument
        if city:
            filter = (
                Q(city__icontains=city)
            )
            courts = courts.filter(filter)

        # if state argument is given, return courts with name containing argument
        if state:
            filter = (
                Q(state__icontains=state)
            )
            courts = courts.filter(filter)

        # if skip is given, skip n values
        if skip:
            courts = courts[skip:]

        # if first is given, return only that many objects
        if first:
            courts = courts[:first]
        return courts


    # Return all map styles to endpoint
    def resolve_all_map_styles(self, info, mapstyle=None, first=None, skip=None, **kwargs):
        mapstyles = MapStyle.objects.all()

        # if state argument is given, return courts with name containing argument
        if mapstyle:
            filter = (
                Q(mapstyle__icontains=mapstyle)
            )
            mapstyles = MapStyle.objects.filter(filter)

        # if skip is given, skip n values
        if skip:
            mapstyles = mapstyles[skip:]

        # if first is given, return only that many objects
        if first:
            mapstyles = mapstyles[:first]

        return mapstyles

    # Return all map api keys to endpoint
    def resolve_all_map_api_key(self, info, **kwargs):
        return MapAPIKey.objects.all()

    # Return all user signups to endpoint
    def resolve_all_signups(self, info, first=None, skip=None, **kwargs):
        signups = Signup.objects.all()

        # if skip is given, skip n values
        if skip:
            signups = signups[skip:]

        # if first is given, return only that many objects
        if first:
            signups = signups[:first]

        return signups
