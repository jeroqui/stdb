import graphene

class Query(graphene.ObjectType):
    test = graphene.String()

    def resolve_test(self, info):
        return "It works"

schema = graphene.Schema(query=Query)
