from django.urls import path

from .views import (
    home,
    geopolitics,
    geopolitics_article,
    geopolitics_region,
)

urlpatterns = [
    path("", home, name="home"),
    path("geopolitics/", geopolitics, name="geopolitics"),
    path("geopolitics/<slug:region>/<slug:slug>/", geopolitics_article, name="geopolitics_article"),
    path("geopolitics/<slug:region>/", geopolitics_region, name="geopolitics_region"),
]
