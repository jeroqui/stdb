import graphene
from graphene_django import DjangoObjectType, DjangoListField 

from src.modules.apps.vampire.schema.types import HumanType
from ..models import Character, CharacterRelationship, Chronicle, Plot, PlotStages, Sesion, Event

from src.modules.utils.schema.scalars import PublicId


class PublicIdInterface(graphene.Interface):
    # I haven't been able to figure out how to convert the id to public from the interface
    # so that logic is handled through a Graphene middleware
    ...



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
        fields = ("id", "chronicle", "name", "story", "pc", "humancc", "vampirecc")


    relationships = DjangoListField(CharacterRelationshipType)

    def resolve_relationships(parent, info):
        return CharacterRelationship.objects.filter(character1=parent)


class PlotType(DjangoObjectType):
    class Meta:
        model = Plot

class PlotStagesType(DjangoObjectType):
    class Meta:
        model = PlotStages
        fields = ("id", "description")

class SesionType(DjangoObjectType):
    class Meta:
        model = Sesion

class EventType(DjangoObjectType):
    class Meta:
        model = Event