import graphene
from graphene_django import DjangoObjectType, DjangoListField 


from src.modules.utils.schema import CustomNode
from ..models import Character, CharacterRelationship, Chronicle


class ChronicleType(DjangoObjectType):
    class Meta:
        model = Chronicle
        filter_fields = ['name']
        fields = ("id", "name")
        interfaces = ()

class CharacterRelationshipType(DjangoObjectType):
    class Meta:
        model = CharacterRelationship
        fields = ("id", "feeling", "character2")

class CharacterType(DjangoObjectType):
    class Meta:
        model = Character
        filter_fields = ['chronicle']
        fields = ("id", "chronicle", "name", "story", "pc")
        interfaces = ()

    relationships = DjangoListField(CharacterRelationshipType)

    def resolve_relationships(parent, info):
        return CharacterRelationship.objects.filter(character1=parent)
    