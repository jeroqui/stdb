from django.forms import ModelForm

from src.modules.apps.core.models import Character

class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ["chronicle", "name", "story", "pc"]