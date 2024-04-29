import json
import re
import time

import requests
import urllib3
from Crypto.Cipher import AES
import base64

from lib.tool import wirte_data, req
from settings import DATA_PATH

urllib3.disable_warnings()


class ComAtomxVeeevpn:
    def __init__(self, app):
        self.headers = {
            'accept': 'application/json, text/plain, */*',
            'token': 'BN1QfVPt6XAVwBe1+Ufh2j+r0jWFVwXrwEG3ayBuTwCw6AbIPzp61pnKTyJcrDeLrwx0yfz8zajwYAxegyyRmahOIiozJFmz9UuNmyuAYqpcL/rCNvf7ky25xIQMVSFoRJtC0BAJyZ3CNLbB/9rOdB12Pd3iU12rC2ZqBhHQYBH91rPScCQuQqciyBN+5CZsrXpKZ1CDhph25Yi6SrEpOVwwBdmbprUk6ATOqjYzUb6TAeMO75gZXtkQPw==',
            # 'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiIzMjI3Nzk1IiwiaXNzIjoiYXBpLnZlZWUiLCJpYXQiOjE2OTQ2NTM0NTAsImV4cCI6MTY5NzI0NTQ1MCwidEtleSI6IjNmMDM5MWQxYTFlN2NlOWRiOTAxNzQzYjQ1ZjBlNTY5In0.k5kfBH6I4AVxto_7K5nDUtasH097dgvdMm3KxKGJrXM',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Content-Length': '261',
            'Host': 'cdn.taptap123.com:9527',
            # https://cdn.taptap123.com:9527
            # 'Host': 'https://e.tapdb.net:9527',
            # 'Host': '199.180.114.129:3000',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/4.9.2',
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        datas = json.loads(self.decrypt(base64.b64decode(self.get_iplist())))
        print(datas)
        # print(datas["bean"])
        # for data in datas["bean"]["list"]:
        #     lineId = data["id"]
        #     res = self.decrypt(base64.b64decode(self.get_ipinfo(lineId)))
        #     print(res)
        #     if not json.loads(res)["bean"]:
        #         return
        #     wirte_data(res + "\n", self.path_name)

    def decrypt(self, text):
        key = "KvDDCwNqVqYMcKWA".encode('utf-8')
        iv = "ncgJwfftebJjGUcs".encode('utf-8')
        cryptos = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
        plain_text = cryptos.decrypt(text)
        return plain_text.decode()

    def encrypt(self, text):
        key = "KvDDCwNqVqYMcKWA".encode('utf-8')
        iv = "ncgJwfftebJjGUcs".encode('utf-8')
        cryptos = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
        plain_text = cryptos.encrypt(text.encode())
        return base64.b64encode(plain_text).decode()

    def get_ipinfo(self, lineId):
        time.sleep(3)
        url = f"https://cdn.taptap123.com:9527/func/linkBegin"
        # url = f'https://199.180.114.129:3000/func/linkBegin'
        params = {
            "lineId": lineId,
            "model": "Pixel XL",
            "deviceId": "f20f6f5e-c07c-44e0-a8b2-3189f1",
            "platform": "MOBILE",
            "os": "android",
            "osVersion": "8.1.0",
            "pv": 3
        }
        data = {
            '_params': self.encrypt(json.dumps(params)),
            '_pv': '1',
        }
        response = req(url, headers=self.headers, data=data, method="post")
        print(response.text)
        return response.text

    def get_iplist(self):
        time.sleep(3)
        url = f"https://cdn.taptap123.com:9527/func/linkList"
        # url = f"https://cdn.tapdb-dev.com:9527/func/linkList"
        # url = f'https://199.180.114.129:3000/func/linkBegin'
        # https://cdn.sqweli.vip:9527
        data = {
            '_params': '',
            '_pv': '',
        }
        response = req(url, headers=self.headers, method="post")
        print(url)
        print(response.status_code)
        print(response.text)
        return response.text


if __name__ == '__main__':
    app = {
        'appPackage': 'com.atomx.veeevpn',
        'package': 'com.atomx.veeevpn',
        'appActivity': '',
        'click_file': 'com_atomx_veeevpn',
        'process': 'com_atomx_veeevpn',
        'data': 'com_atomx_veeevpn',
        'data_type': 'data',
        'class_name': '',
        'type': 'request',
    }
    c = ComAtomxVeeevpn(app)
    c.main()
    # link = "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"
    # a = base64.b64decode(link)
    # print(c.decrypt(a))
    # c.get_iplist()
    # c.get_ipinfo(108)
