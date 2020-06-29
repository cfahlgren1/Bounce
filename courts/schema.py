import graphene, graphql_geojson, uuid
from graphql import GraphQLError
from graphql_auth.schema import UserQuery, MeQuery
import graphene_django_optimizer as gql_optimizer
from graphql_auth import mutations
from django.db.models import Q
from graphene_django.types import DjangoObjectType
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
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
    closest_courts_to = graphene.List(CourtType, lat=graphene.Float(), lng=graphene.Float(), category=graphene.String(), first=graphene.Int(), skip=graphene.Int())
    all_soccer_fields = graphene.List(CourtType, id=graphene.ID(), name=graphene.String(), city=graphene.String(), state=graphene.String(), first=graphene.Int(), skip=graphene.Int())
    all_tennis_courts = graphene.List(CourtType, id=graphene.ID(), name=graphene.String(), city=graphene.String(), state=graphene.String(), first=graphene.Int(), skip=graphene.Int())
    all_map_styles = graphene.List(MapStyleType, mapstyle=graphene.String(), first=graphene.Int(), skip=graphene.Int())
    all_map_api_key = graphene.List(MapAPIKeyType)
    all_signups = graphene.List(SignupType, first=graphene.Int(), skip=graphene.Int())

    # Return all basketball courts to endpoint
    def resolve_all_basketball_courts(self, info, id=None, name=None, city=None, state=None, first=None, skip=None, **kwargs):
        # use authentication with jwt tokens
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('Not logged in!')

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

        # optimize query with select_related and prefetch_related
        courts = gql_optimizer.query(courts,info)

        # if skip is given, skip n values
        if skip:
            courts = courts[skip:]

        # if first is given, return only that many objects
        if first:
            courts = courts[:first]

        return courts

    def resolve_closest_courts_to(self, info, lat, lng, category, first=None, skip=None, **kwargs):
        # use authentication with jwt tokens
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('Not logged in!')

        searched_location = Point(lat, lng, srid=4326)
        courts = Court.objects.annotate(distance=Distance('location',searched_location)).order_by('distance').filter(category=category)

        # optimize query with select_related and prefetch_related
        courts = gql_optimizer.query(courts, info)

        # if skip is given, skip n values
        if skip:
            courts = courts[skip:]

        # if first is given, return only that many objects
        if first:
            courts = courts[:first]

        return courts

    # Return all tennis courts to endpoint
    def resolve_all_tennis_courts(self, info, id=None, name=None, city=None, state=None, first=None, skip=None, **kwargs):
        # use authentication with jwt tokens
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('Not logged in!')

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

        # optimize query with select_related and prefetch_related
        courts = gql_optimizer.query(courts, info)

        # if skip is given, skip n values
        if skip:
            courts = courts[skip:]

        # if first is given, return only that many objects
        if first:
            courts = courts[:first]
        return courts

    # Return all soccer fields to endpoint
    def resolve_all_soccer_fields(self, info, id=None, name=None, city=None, state=None, first=None, skip=None, **kwargs):
        # use authentication with jwt tokens
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('Not logged in!')

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

        # optimize query with select_related and prefetch_related
        courts = gql_optimizer.query(courts, info)

        # if skip is given, skip n values
        if skip:
            courts = courts[skip:]

        # if first is given, return only that many objects
        if first:
            courts = courts[:first]
        return courts


    # Return all map styles to endpoint
    def resolve_all_map_styles(self, info, mapstyle=None, first=None, skip=None, **kwargs):
        # use authentication with jwt tokens
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('Not logged in!')

        mapstyles = MapStyle.objects.all()

        # if state argument is given, return courts with name containing argument
        if mapstyle:
            filter = (
                Q(mapstyle__icontains=mapstyle)
            )
            mapstyles = MapStyle.objects.filter(filter)

        # optimize query with select_related and prefetch_related
        mapstyles = gql_optimizer.query(mapstyles, info)

        # if skip is given, skip n values
        if skip:
            mapstyles = mapstyles[skip:]

        # if first is given, return only that many objects
        if first:
            mapstyles = mapstyles[:first]

        return mapstyles

    # Return all map api keys to endpoint
    def resolve_all_map_api_key(self, info, **kwargs):
        # use authentication with jwt tokens
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('Not logged in!')

        return gql_optimizer.query(MapAPIKey.objects.all(), info)

    # Return all user signups to endpoint
    def resolve_all_signups(self, info, first=None, skip=None, **kwargs):
        # use authentication with jwt tokens
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('Not logged in!')

        signups = gql_optimizer.query(Signup.objects.all(), info)

        # if skip is given, skip n values
        if skip:
            signups = signups[skip:]

        # if first is given, return only that many objects
        if first:
            signups = signups[:first]

        return signups

class CreateCourt(graphene.Mutation):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()
    house_number = graphene.String()
    road = graphene.String()
    city = graphene.String()
    zip_code = graphene.String()
    state = graphene.String()
    country = graphene.String()

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()
        house_number = graphene.String(required=True)
        road = graphene.String(required=True)
        city = graphene.String(required=True)
        zip_code = graphene.String(required=True)
        state = graphene.String(required=True)
        country = graphene.String()
        lng = graphene.Float(required=True)
        lat = graphene.Float(required=True)
        category = graphene.String()

    def mutate(self, info, name, description="", house_number="", road=None, city=None, zip_code=None, state=None, country=None, lng=None, lat=None, category="Basketball"):
        location = Point(lat, lng, srid=4326)
        # check if court already exists
        if Court.objects.filter(location=location).count() == 0:
            court = Court(id=uuid.uuid4(), name=name, description=description, house_number=house_number, road=road, city=city, zip_code=zip_code, state=state, country=country, location=location, category=category)
            court.save()

            return CreateCourt(
                id=court.id,
                name=court.name,
                description=court.description,
                house_number=court.house_number,
                road=court.road,
                city=court.city,
                zip_code=court.zip_code,
                state=court.state,
                country=court.country,
            )
        raise GraphQLError("Court with that location already exists!")


class Mutation(graphene.ObjectType):
    create_court = CreateCourt.Field()

    # GraphQL Authentication
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()
    update_account = mutations.UpdateAccount.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()
