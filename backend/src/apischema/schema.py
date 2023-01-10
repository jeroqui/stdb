import graphene

from src.modules.apps.core.schema.query import Query as CoreQuery

class Query(CoreQuery, graphene.ObjectType):
    test = graphene.String()

    def resolve_test(self, info):
        return "It works"

schema = graphene.Schema(query=Query)
