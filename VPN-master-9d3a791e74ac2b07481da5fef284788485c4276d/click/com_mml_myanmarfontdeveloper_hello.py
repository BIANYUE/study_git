# -*- coding: utf-8 -*-
import base64
import binascii
import hashlib
import json
import random
import re
import time
from urllib.parse import urlencode

from Crypto.Cipher import AES

from lib.tool import req, wirte_data
from settings import DATA_PATH


class ComMmlMyanmarfontdeveloperHello:
    def __init__(self, app):
        self.headers = {
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; Pixel XL Build/OPM4.171019.021.P1)',
            'Host': 'dfybhjkk2435.sgp1.digitaloceanspaces.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        iplist = self.get_iplist()
        for ip in iplist:
            url = ip["so"]
            datas = self.get_ip(url)
            data = re.search("nobind(.*?)dev tun", datas, re.S).group(1).strip()
            print(data)
            # print(type(data))
            wirte_data(data + "\n", self.path_name)

    def get_iplist(self):
        # time.sleep(3)
        url = f"https://dfybhjkk2435.sgp1.digitaloceanspaces.com/hellovpn/json/hellovpn.json"
        response = req(url, headers=self.headers)
        print(response.text)
        return json.loads(response.text)

    def get_ip(self, url):
        response = req(url, headers=self.headers)
        # print(response.text)
        return response.text



if __name__ == '__main__':
    app = {
        'appPackage': 'com.mml.myanmarfontdeveloper.hello',
        'package': 'com.mml.myanmarfontdeveloper.hello',
        'appActivity': '',
        'click_file': 'com_mml_myanmarfontdeveloper_hello',
        'process': 'com_mml_myanmarfontdeveloper_hello',
        'data': 'com_mml_myanmarfontdeveloper_hello',
        'data_type': 'data',
        'class_name': '',
        'type': 'request',
    }
    cpa = ComMmlMyanmarfontdeveloperHello(app)
    cpa.main()
