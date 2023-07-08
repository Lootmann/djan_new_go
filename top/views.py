from django.shortcuts import render
from django.views import generic


class TopIndexView(generic.TemplateView):
    template_name = "top/index.html"
