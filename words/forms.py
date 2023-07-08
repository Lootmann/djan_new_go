from django.forms import ModelForm

from examples.models import WordModel


class WordForm(ModelForm):
    class Meta:
        model = WordModel
        fields = ["spell", "meaning"]
