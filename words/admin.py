from django.contrib import admin

from words.models import WordModel


@admin.register(WordModel)
class WordAdmin(admin.ModelAdmin):
    pass
