from django.http import HttpRequest
from django.shortcuts import render
from django.views import generic

from examples.forms import ExampleForm
from words.forms import WordForm


class RegistersIndexView(generic.View):
    template_name = "registers/index.html"
    word_form = WordForm
    example_form = ExampleForm

    def get(self, request: HttpRequest, *args, **kwargs):
        return render(
            request,
            self.template_name,
            {"word_form": self.word_form(), "example_form": self.example_form()},
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        # words
        f = WordForm(request.POST)

        if f.is_valid():
            f.save()

            # examples
            f = ExampleForm(request.POST)
            print(f)

        else:
            return render(
                request,
                self.template_name,
                {"word_form": self.word_form(), "example_form": self.example_form()},
            )
