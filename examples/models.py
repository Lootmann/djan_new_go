from django.db import models

from words.models import WordModel


class ExampleModel(models.Model):
    sentence = models.TextField(blank=True)
    translation = models.TextField(blank=True)
    word = models.ForeignKey(WordModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.sentence}"
