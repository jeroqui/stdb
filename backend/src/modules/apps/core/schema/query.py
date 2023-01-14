import graphene

from . import types as coretypes
from src.modules.utils.schema import PublicId

from src.modules.apps.core.models import Character, Chronicle, Plot, Sesion


class Query(graphene.ObjectType):
    chronicles = graphene.List(coretypes.ChronicleType)
    def resolve_chronicles(self, info):
        return Chronicle.objects.all()
    

    character = graphene.Field(coretypes.CharacterType)
    chronicle_characters = graphene.List(coretypes.CharacterType, chronicle=PublicId(required=True))
    def resolve_character(self, info, id):
        return Character.objects.get(pk=id)

    def resolve_chronicle_characters(self, info, chronicle):
        chronicle_obj = Chronicle.objects.filter(pk=chronicle).first()
        if not chronicle:
            return Character.objects.none()

        return Character.objects.filter(chronicle=chronicle_obj)



    chronicle_plots = graphene.List(coretypes.PlotType, chronicle=PublicId(required=True))
    def resolve_chronicle_plots(self, info, chronicle):
        chronicle_obj = Chronicle.objects.filter(pk=chronicle).first()
        if not chronicle:
            return Plot.objects.none()
        
        return Plot.objects.filter(chronicle=chronicle_obj)
        
    chronicle_sesions = graphene.List(coretypes.SesionType, chronicle=PublicId(required=True))
    def resolve_chronicle_sesions(self, info, chronicle):
        chronicle_obj = Chronicle.objects.filter(pk=chronicle).first()
        if not chronicle:
            return Sesion.objects.none()
        
        return Sesion.objects.filter(chronicle=chronicle_obj)
        
