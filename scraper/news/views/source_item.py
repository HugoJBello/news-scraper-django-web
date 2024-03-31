from django.shortcuts import render
from django.http import HttpResponse
from ..managers.api_manager import ApiManager

api_manager = ApiManager()

def source_item(request, source_id):
    index = api_manager.get_index(source_id)
    data = {"logo_url": "test", "newspaper":"test", "index": index} 

    return render(request, "../templates/source_item.html", data)
