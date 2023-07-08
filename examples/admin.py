from django.contrib import admin

from examples.models import ExampleModel


@admin.register(ExampleModel)
class ExampleAdmin(admin.ModelAdmin):
    pass
