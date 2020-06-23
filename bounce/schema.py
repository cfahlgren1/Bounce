import graphene
from courts.schema import Query as court_query
from courts.schema import Mutation as court_mutation


class Query(court_query):
    pass

class Mutation(court_mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)