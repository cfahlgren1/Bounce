import graphene
from graphql_auth.schema import UserQuery, MeQuery
from courts.schema import Query as court_query
from courts.schema import Mutation as court_mutation


class Query(court_query, UserQuery, MeQuery, graphene.ObjectType):
    pass

class Mutation(court_mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)