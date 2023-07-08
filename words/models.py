from django.db import models


class WordModel(models.Model):
    spell = models.CharField(max_length=50)
    meaning = models.TextField()

    def __str__(self) -> str:
        return f"{self.spell}"
