from django.forms import ModelForm

from examples.models import ExampleModel


class ExampleForm(ModelForm):
    class Meta:
        model = ExampleModel
        fields = ["sentence", "translation"]
