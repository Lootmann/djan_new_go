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
        f = WordForm(request.POST)

        if not f.is_valid():
            return render(
                request,
                self.template_name,
                {"word_form": f, "example_form": self.example_form()},
            )

        # WordForm is valid
        word_model = f.save()

        # examples
        f = ExampleForm(request.POST)

        if not f.is_valid():
            return render(
                request,
                self.template_name,
                {"word_form": self.word_form(), "example_form": self.example_form()},
            )

        new_example = f.save(commit=False)
        new_example.word = word_model
        new_example.save()

        return render(
            request,
            self.template_name,
            {"word_form": self.word_form(), "example_form": self.example_form()},
        )
