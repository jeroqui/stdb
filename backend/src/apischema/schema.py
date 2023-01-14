import graphene

from src.modules.apps.core.schema.query import Query as CoreQuery
from src.modules.apps.core.schema.mutations import Mutation as CoreMutation


class Query(CoreQuery, graphene.ObjectType):
    test = graphene.String()

    def resolve_test(self, info):
        return "It works"


class Mutation(CoreMutation, graphene.ObjectType):
    ...


schema = graphene.Schema(query=Query, mutation=Mutation)
