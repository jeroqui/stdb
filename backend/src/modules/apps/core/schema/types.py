from graphene_django import DjangoObjectType, DjangoListField 

from ..models import Character, CharacterRelationship, Chronicle


class ChronicleType(DjangoObjectType):
    class Meta:
        model = Chronicle
        fields = ("id", "name")

class CharacterRelationshipType(DjangoObjectType):
    class Meta:
        model = CharacterRelationship
        fields = ("id", "feeling", "character2")

class CharacterType(DjangoObjectType):
    class Meta:
        model = Character
        fields = ("id", "chronicle", "name", "story", "pc")


    relationships = DjangoListField(CharacterRelationshipType)

    def resolve_relationships(parent, info):
        return CharacterRelationship.objects.filter(character1=parent)
    