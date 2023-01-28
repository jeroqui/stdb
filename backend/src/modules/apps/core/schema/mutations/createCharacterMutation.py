import graphene

from src.modules.utils.schema.scalars import PublicId
from src.modules.utils.schema.mutations import FormErrorMutation

from ..types import CharacterType
from src.modules.apps.core.forms import CharacterForm

class CreateCharacterInput(graphene.InputObjectType):
    chronicle = PublicId(required=True)
    name = graphene.String(required=True)
    story = graphene.String()
    pc = graphene.Boolean()


class CreateCharacterMutation(FormErrorMutation):
    class Arguments:
        input = CreateCharacterInput(required=True)

    class Meta:
        form_class = CharacterForm

    character = graphene.Field(CharacterType)

    # def mutate(root, info, input=None):
    #     character = CharacterForm(input)

    #     if character.is_valid():
    #         return CreateCharacterMutation(character=character.save())
