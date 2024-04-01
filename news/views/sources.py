from django.shortcuts import render
from django.http import HttpResponse
from ..managers.api_manager import ApiManager
import timeago, datetime

api_manager = ApiManager()

def sources(request):
    indexes = api_manager.get_all_indexes()
    now = datetime.datetime.now()

    for index in indexes:
        index["link"] = "/news/source_item/" + str(index["newspaper"])
        index["date_from_now"] = timeago.format(datetime.datetime.strptime(index["dateScraping"], '%Y-%m-%dT%H:%M:%S.%fZ'), now)

    data = {"indexes": indexes} 

    return render(request, "../templates/sources.html", data)
