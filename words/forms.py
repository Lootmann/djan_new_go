from django import forms
from django.forms import ModelForm

from words.models import WordModel


class WordForm(ModelForm):
    class Meta:
        model = WordModel
        fields = ["spell", "meaning"]

    def clean_spell(self):
        # check whether spell is duplicated
        spell = self.cleaned_data["spell"]

        if WordModel.objects.filter(spell__iexact=spell).exists():
            raise forms.ValidationError(f"spell: {spell} is duplicated :^)")

        return spell

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
