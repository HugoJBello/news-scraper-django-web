from django.shortcuts import render
from django.http import HttpResponse
from ..managers.api_manager import ApiManager

api_manager = ApiManager()

def sources(request):
    response = "sources"
    data = {"content": "Gfg is the best"} 

    #api_manager.get_all_indexes()
    return render(request, "../templates/sources.html", data)

def source_item(request, source_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % source_id)