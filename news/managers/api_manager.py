import os
import requests

default_api_url = os.getenv("API_URL")

class ApiManager:
    
    api_url = ""
    def __init__(self):
        self.api_url = default_api_url
        
    def get_all_indexes(self):
        url =self.api_url + "/api/v1/scrapingIndex/findQuery?&limit=99999&orderByParam=createdAt&orderDirection=ASC"
        resp = requests.get(url)
        return resp.json()["payload"]["rows"]
    
    
    def get_index(self, newspaper:str):
        url = self.api_url + "/api/v1/scrapingIndex/findQuery?&limit=1&newspaper=" + newspaper
        resp = requests.get(url)
        return resp.json()["payload"]["rows"][0]
    
    def get_news_item(self, id:str):
        url = self.api_url + "/api/v1/newScraped/findQuery?&limit=1&id=" + id
        resp = requests.get(url)
        return resp.json()["payload"]["rows"][0]
 
    def get_results_in_newspaper(self, newspaper:str):
        url = self.api_url + "/api/v1/resultsInNewspaper/find?newspaper=" + newspaper
        resp = requests.get(url)
        return resp.json()["payload"]
  
    def get_global_config(self):
        url = self.api_url + "/api/v1/globalConfig/findQuery?limit=9999&orderByParam=createdAt&orderDirection=DESC"
        resp = requests.get(url)
        return resp.json()["payload"]["rows"][0]