import graphene
from courts.schema import Query as court_query

class Query(court_query):
    pass

schema = graphene.Schema(query=Query)