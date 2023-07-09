from django.contrib import admin

from examples.models import ExampleModel


@admin.register(ExampleModel)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ("id", "sentence", "translation")
    ordering = ["sentence"]
