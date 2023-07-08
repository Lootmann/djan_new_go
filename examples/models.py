from django.db import models

from words.models import WordModel


class ExampleModel(models.Model):
    sentence = models.TextField()
    translation = models.TextField()
    word = models.ForeignKey(WordModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"[{self.word.spell}] {self.sentence}"
