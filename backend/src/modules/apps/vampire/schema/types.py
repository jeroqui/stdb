from graphene_django import DjangoObjectType

# from src.modules.apps.core.schema.types import CharacterType
from ..models import HumanCC, VampireCC

class HumanType(DjangoObjectType):
    class Meta:
        model = HumanCC
        fields = ("__all__")

class VampireType(DjangoObjectType):
    class Meta:
        model = VampireCC