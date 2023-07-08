from django.urls import path

from top.views import TopIndexView

app_name = "top"

urlpatterns = [
    path("", TopIndexView.as_view(), name="index"),
]
