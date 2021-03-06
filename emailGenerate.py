import json
import hashlib
from typing import List

import requests

from models import mail_from_dict, Mail


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

    def get_hash(self, email):
        md5_hash = hashlib.md5()
        md5_hash.update(bytes(email, 'utf-8'))

        hash_value = md5_hash.hexdigest()
        return hash_value

    def check_email(self, hash_value) -> Mail:
        url = self.url + f"/mail/id/{hash_value}/"
        payload = {}
        response = json.loads(requests.request("GET", url, headers=self.header, data=payload).text)
        mailDict = {
            "error": None,
            "data": []
        }
        if isinstance(response, List):
            mailDict["data"] = response
        else:
            mailDict["error"] = response["error"]
        return mail_from_dict(mailDict)



