from random import choice

from django.shortcuts import render
from django.views import generic

from words.models import WordModel


class QuizView(generic.View):
    template_name = "quiz/index.html"

    def get(self, request, *args, **kwargs):
        pks = WordModel.objects.values_list("pk", flat=True)
        random_pk = choice(pks)
        word = WordModel.objects.get(pk=random_pk)
        return render(request, self.template_name, {"word": word})
