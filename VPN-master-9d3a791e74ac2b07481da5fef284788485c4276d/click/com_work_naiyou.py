# -*- coding: utf-8 -*-
import time
import requests
# from click.base_appnium import BaseAppium
from lib.tool import wirte_data, req
from settings import DATA_PATH
import urllib3
urllib3.disable_warnings()


# com.work.naiyou
class ComWorkNaiyou:
    def __init__(self, app):
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        ip_list = self.get_iplist()
        print(ip_list)
        wirte_data(ip_list + "\n", self.path_name)

    def get_iplist(self):
        url = "http://api.ruanjian1.buzz/api/client/v4/nodes"
        headers = {
            'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmFuZHJvaWRyajAxLnRvcFwvYXBpXC9jbGllbnRcL3YzXC9sb2dpbiIsImlhdCI6MTY5MjI2NTM5NiwiZXhwIjoxNzI4NTUzMzk2LCJuYmYiOjE2OTIyNjUzOTYsImp0aSI6IldmNHdWZXE1aFBTWnVDeGMiLCJzdWIiOjkwODc5MywicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.saUtfnVMQPL36XG6Uoz-vEQY44ftpt16JRgtGA07PJI',
            'device': 'Android',
            'accept-encoding': 'gzip',
            'user-agent': 'okhttp/4.9.0',
        }
        response = req(url, headers=headers)
        # print(response)
        return response.text


if __name__ == '__main__':
    app = {
        'appPackage': 'com.work.naiyou',
        'package': 'com.work.naiyou',
        'appActivity': '',
        'click_file': 'com_work_naiyou',
        'process': 'com_work_naiyou',
        'data': 'com_work_naiyou',
        'data_type': 'password',
        'class_name': '',
        'type': 'request',
    }
    c = ComWorkNaiyou(app)
    # d = c.decrypt(base64.b64decode("Jo28JKEhznEnAMCi5y9Phg=="))
    # print(d)
    c.main()
