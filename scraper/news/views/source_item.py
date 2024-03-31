from django.shortcuts import render
from django.http import HttpResponse
from ..managers.api_manager import ApiManager

api_manager = ApiManager()

def source_item(request, source_id):
    results = api_manager.get_results_in_newspaper(source_id)
    index = results["scrapingIndex"]
    news = results["news"]
    for new in news:
        new["link"] = "/news/new/" + str(new["id"])
    data = {"logo_url": "test", "newspaper":source_id, "index": index, "news":news} 

    return render(request, "../templates/source_item.html", data)

