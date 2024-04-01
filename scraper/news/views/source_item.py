from django.shortcuts import render
from django.http import HttpResponse
from ..managers.api_manager import ApiManager
import timeago, datetime

api_manager = ApiManager()

def source_item(request, source_id):
    results = api_manager.get_results_in_newspaper(source_id)
    index = results["scrapingIndex"]
    news = results["news"]
    now = datetime.datetime.now()

    for new in news:
        new["link"] = "/news/new/" + str(new["id"])
        new["date_from_now"] = timeago.format(datetime.datetime.strptime(new["scrapedAt"], '%Y-%m-%dT%H:%M:%S.%fZ'), now)
    data = {"newspaper":source_id, "index": index, "news":news} 

    return render(request, "../templates/source_item.html", data)

