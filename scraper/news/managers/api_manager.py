import requests
default_api_url = "https://pettier-kiwi-7067.dataplicity.io/news"

class ApiManager:
    api_url = ""
    def __init__(self, api_url:str = default_api_url):
        self.api_url = api_url
        
    def get_all_indexes(self):
        url =self.api_url + "/api/v1/scrapingIndex/findQuery?&limit=99999&orderByParam=createdAt&orderDirection=ASC"
        resp = requests.get(url)
        return resp.json()["payload"]["rows"]
    
    
    def get_index(self, newspaper:str):
        url = self.api_url + "/api/v1/scrapingIndex/findQuery?&limit=1&newspaper=" + newspaper
        resp = requests.get(url)
        return resp.json()["payload"]["rows"][0]
    
    def get_news_item(self, newspaper:str):
        url = self.api_url + "/api/v1/resultsInNewspaper/find?newspaper=" + newspaper
        resp = requests.get(url)
        return resp.json()["payload"]["rows"]

    
    def get_global_config(self):
        url = self.api_url + "/api/v1/globalConfig/findQuery?limit=9999&orderByParam=createdAt&orderDirection=DESC"
        resp = requests.get(url)
        return resp.json()["payload"]["rows"][0]