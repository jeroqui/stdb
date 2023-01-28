import graphene
import graphql_jwt

from src.modules.apps.core.schema.query import Query as CoreQuery
from src.modules.apps.core.schema.mutations import Mutation as CoreMutation


class Query(CoreQuery, graphene.ObjectType):
    test = graphene.String()

    def resolve_test(self, info):
        return "It works"


class Mutation(CoreMutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    ...


schema = graphene.Schema(query=Query, mutation=Mutation)
