from django.urls import path

from registers.views import RegistersIndexView

app_name = "registers"

urlpatterns = [
    path("", RegistersIndexView.as_view(), name="index"),
]
