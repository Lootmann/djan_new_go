from django import forms
from django.forms import ModelForm

from examples.models import ExampleModel


class ExampleForm(ModelForm):
    class Meta:
        model = ExampleModel
        fields = ["sentence", "translation"]

    def clean(self):
        cleaned_data = super().clean()
        sentence = cleaned_data["sentence"]
        translation = cleaned_data["translation"]

        # when both sentence and translation are empty,
        # do not save this to ExampleModel.
        if sentence is None or sentence == "":
            if translation is None or translation == "":
                raise forms.ValidationError("Empty")

        return cleaned_data
