from django.urls import path

from words.views import WordListView

app_name = "words"

urlpatterns = [
    path("", WordListView.as_view(), name="index"),
]
