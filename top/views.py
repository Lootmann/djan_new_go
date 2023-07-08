from django.http import HttpRequest
from django.shortcuts import render
from django.views import generic

from examples.models import ExampleModel
from words.models import WordModel


class TopIndexView(generic.TemplateView):
    template_name = "top/index.html"

    def get(self, request: HttpRequest, *args, **kwargs):
        context = {
            "words": WordModel.objects.all(),
            "examples": ExampleModel.objects.all(),
        }
        return render(request, self.template_name, context)
