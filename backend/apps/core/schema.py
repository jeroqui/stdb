import graphene
from graphene_django import DjangoObjectType

from .models import Character

class CharacterType(DjangoObjectType):
    class Meta:
        model = Character