import json
import hashlib
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
        return json.loads(response.text)

    def generate_email(self, email):
        md5_hash = hashlib.md5()
        md5_hash.update(bytes(email, 'utf-8'))

        hash_value = md5_hash.hexdigest()
        return hash_value

    def check_email(self, hash_value):
        url = self.url + f"/mail/id/{hash_value}/"
        payload = {}
        response = requests.request("GET", url, headers=self.header, data=payload)
        return json.loads(response.text)



