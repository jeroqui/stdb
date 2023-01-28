import graphene

from . import types as coretypes
from src.modules.apps.vampire.schema import types as vampiretypes
from src.modules.utils.schema.scalars import PublicId

from src.modules.apps.core.models import Character, Chronicle, Plot, Sesion


class Query(graphene.ObjectType):
    chronicles = graphene.List(coretypes.ChronicleType)
    def resolve_chronicles(self, info):
        if info.context.user.is_authenticated:
            if info.context.user.is_admin:
                return Chronicle.objects.all()
        
            return Chronicle.objects.filter(players__in=info.context.user)
        
        return Chronicle.objects.none()
    

    character = graphene.Field(coretypes.CharacterType, id=PublicId(required=True))
    chronicle_characters = graphene.List(coretypes.CharacterType, chronicle=PublicId(required=True))
    def resolve_character(self, info, id):
        if not info.context.user.is_authenticated:
            return Character.objects.none()
        
        character = Character.objects.get(pk=id)

        if info.context.user.is_admin:
            return character

        # TODO: Handle player permissions

    def resolve_chronicle_characters(self, info, chronicle):
        chronicle_obj = Chronicle.objects.filter(pk=chronicle).first()
        if not chronicle_obj:
            return Character.objects.none()

        return Character.objects.filter(chronicle=chronicle_obj)



    chronicle_plots = graphene.List(coretypes.PlotType, chronicle=PublicId(required=True))
    def resolve_chronicle_plots(self, info, chronicle):
        chronicle_obj = Chronicle.objects.filter(pk=chronicle).first()
        if not chronicle_obj:
            return Plot.objects.none()
        
        return Plot.objects.filter(chronicle=chronicle_obj)
        
    chronicle_sesions = graphene.List(coretypes.SesionType, chronicle=PublicId(required=True))
    def resolve_chronicle_sesions(self, info, chronicle):
        chronicle_obj = Chronicle.objects.filter(pk=chronicle).first()
        if not chronicle_obj:
            return Sesion.objects.none()
        
        return Sesion.objects.filter(chronicle=chronicle_obj)
        
