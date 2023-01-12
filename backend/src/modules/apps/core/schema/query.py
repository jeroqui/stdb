import graphene
from graphene_django.filter import DjangoFilterConnectionField

from src.modules.utils.schema import CustomNode
from . import types as coretypes

from src.modules.apps.core.models import Character, Chronicle, CharacterRelationship

class Query(graphene.ObjectType):
    chronicles = graphene.List(coretypes.ChronicleType)
    character = graphene.Field(coretypes.CharacterType)
    chronicle_characters = graphene.List(coretypes.CharacterType, chronicle=graphene.Int(required=True))

    def resolve_chronicles(self, info):
        return Chronicle.objects.all()

    def resolve_character(self, info, id):
        return Character.objects.get(pk=id)

    def resolve_chronicle_characters(self, info, chronicle):
        chronicle = Chronicle.objects.filter(pk=chronicle).first()
        if not chronicle:
            return Character.objects.none()

        return Character.objects.filter(chronicle=chronicle)