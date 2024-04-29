import json
import re
import time

import requests
import urllib3
from Crypto.Cipher import DES
import base64

from lib.tool import wirte_data, req
from settings import DATA_PATH

urllib3.disable_warnings()

# http://8.134.205.49:88
class ComMoguGo:
    def __init__(self, app):
        self.headers = {
            'agentX': 'super-ok-http',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Host': '139.224.69.130:88',
            'Host': '8.134.205.49:88',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/4.2.2',
            'Connection': 'keep-alive',
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        iplist = self.decrypt(base64.b64decode(self.get_iplist()), "92e63a75")
        print(iplist)
        idlist = self.get_idlist(iplist)
        for i in idlist:
            link = self.decrypt(base64.b64decode(self.get_ss(i)), "92e63a75")
            link = re.search('"link":"(.*?)",', link)
            if link:
                ss = self.decrypt(base64.b64decode(link.group(1)), "4a9d9540").replace("\x03", '')
                print(ss)
                wirte_data(ss + "\n", self.path_name)

    def get_idlist(self, iplist):
        idlist = []
        for i in json.loads(iplist)["group"]:
            for j in i["server"]:
                idlist.append(j["id"])
        return idlist

    def decrypt(self, text, key):
        mode = DES.MODE_ECB
        cryptos = DES.new(key.encode('utf-8'), mode)
        plain_text = cryptos.decrypt(text).decode()
        for i in ['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\x09', '\x0a', '\x0b',
                  '\x0c', '\x0d', '\x0e', '\x0f']:
            plain_text = plain_text.replace(i, '')
        return plain_text

    def get_ss(self, i):
        time.sleep(3)
        url = f"http://8.134.205.49:88/api/user/getserver"
        # url = f"http://139.224.69.130:88/api/user/getserver"
        data = {
            'v': '0.97',
            # 'imei': 'di:18d541d067179307',
            'imei': '352530082571746',
            'id': i,
            # 'user': '7993054',
            'user': '10734119',
            'cid': '2',
        }
        response = req(url, headers=self.headers, data=data, method="post")
        # print(response.text)
        return response.text

    def get_iplist(self):
        # time.sleep(3)
        # url = f"http://139.224.69.130:88/api/user/getlist"
        url = f"http://8.134.205.49:88/api/user/getlist"
        data = {
            'v': '0.97',
            #'imei': 'di:18d541d067179307',
            'imei': '352530082571746',
            # 'user': '7993054',
            'user': '10734119',
            'cid': '2',
        }
        response = req(url, headers=self.headers, data=data, method="post")
        print(response.text)
        return response.text


if __name__ == '__main__':
    app = {
        'appPackage': 'com.mogu.go',
        'package': 'com.mogu.go',
        'appActivity': '',
        'click_file': 'com_mogu_go',
        'process': 'com_mogu_go',
        'data': 'com_mogu_go',
        'data_type': 'password',
        'class_name': '',
        'type': 'request',
    }
    c = ComMoguGo(app)
    c.main()
    # link = "wNPBkCdD+Qe8jUwT242SSuf3EdnOwty\/c6I+2Yf3P+bacsZ9HGI2PgL90qUvbIMsJZkFOnwzv84="
    # text = "d898d74eadf5bbdb36ce6d311f9584cbf29388500d3667c2387f850c517ead6cdee1a792d5f4248fd2c338064506a20bc422b831ffb04d80baa260432b4f57c619bfb7ae3da174ba1eb6af45f53d76f5472bfdddcdf4711be64ffcc5c461d06b53aed1b765a7707d19bfb7ae3da174ba5a5069d6b4a566c5f79b9ef1a1c13b44b8820d565d3dd85b21403309737707e9c842e378876e6451068f5f9c0e49d68edcfdb0381fa74f253cb910270a4ee7b021403309737707e9d1fb6a42e59c8f9095afa2d8459d926227771b7f4c03e6375c4ac83b2e6b052e9fd96213fbfb8e775e9fc487df922374af1d349e4fe6d9fa90f9e53fa82e755b983fcf655ea0502412a3ea2c96e76894ddd9def9dc09f42be38aefc588d41fdd"

    # print(c.decrypt(base64.b64decode(link), "4a9d9540").replace("\x03", ''))
    # c.get_iplist()
