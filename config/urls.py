from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # custom apps
    path("", include("top.urls")),
    path("registers/", include("registers.urls")),
    path("words/", include("words.urls")),
    path("quiz/", include("quiz.urls")),
]
