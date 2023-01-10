import graphene
from graphene_django.filter import DjangoFilterConnectionField

from src.modules.utils.schema import CustomNode
from . import types as coretypes

from src.modules.apps.core.models import Character

class Query(graphene.ObjectType):
    character = CustomNode.Field(coretypes.CharacterType)
    chronicle_characters = DjangoFilterConnectionField(coretypes.CharacterType)

    def resolve_ball(self, info, id):
        return Character.objects.get(pk=id)

    def reolve_chronicle_characters(self, info, chronicle_id):
        return Character.objects.filter(chronicle=chronicle_id)