import graphene
from graphene_django import DjangoObjectType

from src.modules.utils.schema import CustomNode
from ..models import Character, CharacterRelationship



class CharacterType(DjangoObjectType):
    class Meta:
        model = Character
        filter_fields = ['chronicle']
        interfaces = (CustomNode, )