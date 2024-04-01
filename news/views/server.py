from django.shortcuts import render
from django.http import HttpResponse
from ..managers.api_manager import ApiManager
import timeago, datetime

api_manager = ApiManager()

def server(request):
    global_config = api_manager.get_global_config()
    now = datetime.datetime.now()

    active_since = datetime.datetime.strptime(global_config["activeSince"], '%Y-%m-%dT%H:%M:%S.%fZ')
    global_config["active_date_from_now"] = timeago.format(active_since, now)
    is_active = active_since > now - datetime.timedelta(minutes=5)
    
    if "\n" in global_config["lastLog"]:
        logs = global_config["lastLog"].split("\n")
    else: 
        logs = [""]
    logs.reverse()
    last_log = logs[0]
    data = {"global_config": global_config, "logs":logs, "last_log":last_log, "is_active":is_active} 

    return render(request, "../templates/server.html", data)
