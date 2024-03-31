from django.shortcuts import render
from django.http import HttpResponse
import markdown

from ..managers.api_manager import ApiManager

api_manager = ApiManager()

def news_item(request, news_id):
    news_item = api_manager.get_news_item(news_id)
    index = api_manager.get_index(news_item["newspaper"])
    md = markdown.Markdown(extensions=["fenced_code"])
    figures = []
    for item in range(len(news_item["figuresUrl"])):
        fig = {"url":news_item["figuresUrl"][item], "text": news_item["figuresText"][item]}
        figures.append(fig)
        
    print(figures)
    news_item["markdown"] = md.convert(news_item["contentMarkdown"])
    data = {"newsItem":news_item, "index": index, "figures":figures} 

    return render(request, "../templates/news_item.html", data)

