from django.views import generic

from words.models import WordModel


class WordListView(generic.ListView):
    model = WordModel
    template_name = "words/words_list.html"
    context_object_name = "words"
