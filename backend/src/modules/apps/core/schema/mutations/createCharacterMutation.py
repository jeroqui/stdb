import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation

from ..types import CharacterType

from src.modules.apps.core.forms import CharacterForm

class CreateCharacterMutation(DjangoModelFormMutation):
    character = graphene.Field(CharacterType)

    class Meta:
        form_class = CharacterForm