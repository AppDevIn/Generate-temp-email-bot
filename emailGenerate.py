import requests


class EmailGenerate:

    def __init__(self, api_key):
        super(EmailGenerate, self).__init__()
        self.host = "privatix-temp-mail-v1.p.rapidapi.com"
        self.api_key = api_key
        self.header = {
            'X-RapidAPI-Host': self.host,
            'X-RapidAPI-Key': self.api_key
        }
        self.url = "https://privatix-temp-mail-v1.p.rapidapi.com/request"

    def get_domains(self):
        url = self.url + "/domains/"
        payload = {}
        response = requests.request("GET", url, headers=self.header, data=payload)
        return response
