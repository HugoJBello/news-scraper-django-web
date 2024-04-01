from django.urls import path

from .views.sources import sources
from .views.source_item import source_item
from .views.news_item import news_item
from .views.server import server
from . import views

urlpatterns = [
    path("sources/", sources, name="sources"),
    path("server/", server, name="server"),
    path("source_item/<str:source_id>/", source_item, name="source_item"),
    path("new/<str:news_id>/", news_item, name="news"),
]