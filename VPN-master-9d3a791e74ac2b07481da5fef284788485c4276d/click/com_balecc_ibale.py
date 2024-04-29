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


class ComBaleccIbale:
    def __init__(self, app):
        self.headers = {
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; Pixel XL Build/OPM4.171019.021.P1)',
            # 'Host': 'djpa.bananaurl.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'keep-alive',
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        res = self.get_iplist()
        # print(res)
        iplist = re.search("proxies:(.*?)proxy-groups:", res, re.S).group(1).strip().split('\n')
        print(iplist)
        for i in iplist:
            print(i)
            if "server: localhost" not in i:
                wirte_data(i.strip() + "\n", self.path_name)

    def get_iplist(self):
        # time.sleep(3)
        # url = f"https://ahk01.bananaurl.com/subscribe/5D6zZhDVPDDy0yLg?clash=1&class=all"
        url = f"https://ibale.store/NCErn/FwYet/chr"
        response = req(url, headers=self.headers)
        # print(response.text)
        return response.text


if __name__ == '__main__':
    app = {
        'appPackage': 'com_balecc_ibale',
        'package': 'com_balecc_ibale',
        'appActivity': '',
        'click_file': 'com_balecc_ibale',
        'process': 'com_balecc_ibale',
        'data': 'com_balecc_ibale',
        'data_type': 'data',
        'class_name': '',
        'type': 'request',
    }
    c = ComBaleccIbale(app)
    c.main()
    # link = "wNPBkCdD+Qe8jUwT242SSuf3EdnOwty\/c6I+2Yf3P+bacsZ9HGI2PgL90qUvbIMsJZkFOnwzv84="
    # print(c.decrypt(base64.b64decode(link), "4a9d9540").replace("\x03", ''))
    # c.get_iplist()
