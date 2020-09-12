import requests
import base64

class pgconn():

    def __init__(self, url, apikey):
        self.url = url
        self.apikey = str(base64.b64encode(apikey.encode("ascii"))).split("\'")[1]  

    def data(self):

        self.header = {'Authorization': 'Basic ' + self.apikey}

        r = requests.get(self.url, headers = self.header)
        return r.json()
        