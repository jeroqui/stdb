import graphene

from .createCharacterMutation import CreateCharacterMutation

class Mutation(graphene.ObjectType):
    create_character = CreateCharacterMutation.Field()