from django.urls import path

from .views.sources import sources
from .views.source_item import source_item
from .views.index import index
from . import views

urlpatterns = [
    path("", index, name="index"),
    path("sources/", sources, name="results"),
    path("source_item/<str:source_id>/", source_item, name="results"),

]