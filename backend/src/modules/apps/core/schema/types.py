import graphene
from graphene_django import DjangoObjectType, DjangoListField 

from src.modules.utils.schema import CustomNode
from ..models import Character, CharacterRelationship


class CharacterRelationshipType(DjangoObjectType):
    class Meta:
        model = CharacterRelationship


class CharacterType(DjangoObjectType):
    class Meta:
        model = Character
        filter_fields = ['chronicle']
        fields = ("id", "chronicle", "name", "story", "pc")
        interfaces = (CustomNode, )

    relationships = DjangoListField(CharacterRelationshipType)

    def resolve_relationships(parent, info):
        return CharacterRelationship.objects.filter(character1=parent)
    