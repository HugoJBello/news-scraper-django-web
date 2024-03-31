from django.shortcuts import render
from django.http import HttpResponse
from ..managers.api_manager import ApiManager

api_manager = ApiManager()

def sources(request):
    indexes = api_manager.get_all_indexes()
    for index in indexes:
        index["link"] = "/news/source_item/" + str(index["newspaper"])
    data = {"indexes": indexes} 

    return render(request, "../templates/sources.html", data)
