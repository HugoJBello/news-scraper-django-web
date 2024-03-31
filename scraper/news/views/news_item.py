from django.shortcuts import render
from django.http import HttpResponse
from ..managers.api_manager import ApiManager

api_manager = ApiManager()

def news_item(request, news_id):
    news_item = api_manager.get_news_item(news_id)
    
    data = { "new":news_item} 

    return render(request, "../templates/news_item.html", data)

