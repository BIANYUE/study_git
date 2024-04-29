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


class ComBananagoNow:
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
        # print(iplist)
        for i in iplist:
            # print(i)
            if "server: localhost" not in i:
                wirte_data(i.strip() + "\n", self.path_name)

    def get_iplist(self):
        # time.sleep(3)
        # https://ahk01.bananaurl.com/subscribe?token=5D6zZhDVPDDy0yLg&type=ssr
        # https://ahk01.bananaurl.com/subscribe?token=5D6zZhDVPDDy0yLg&type=clash
        url = f"https://ahk01.bananaurl.com/subscribe?token=5D6zZhDVPDDy0yLg&type=ssr"
        # url = f"https://ahk01.bananaurl.com/subscribe/5D6zZhDVPDDy0yLg?clash=1&class=all"
        # url = f"https://ahk01.bananaurl.com/subscribe?token=5D6zZhDVPDDy0yLg&type=clash"

        response = req(url, headers=self.headers)
        print(response.text)
        return response.text


if __name__ == '__main__':
    app = {
        'appPackage': 'com.bananago.now',
        'package': 'com.bananago.now',
        'appActivity': '',
        'click_file': 'com_bananago_now',
        'process': 'com_bananago_now',
        'data': 'com_bananago_now',
        'data_type': 'data',
        'class_name': '',
        'type': 'request',
    }
    c = ComBananagoNow(app)
    c.main()
    # link = "wNPBkCdD+Qe8jUwT242SSuf3EdnOwty\/c6I+2Yf3P+bacsZ9HGI2PgL90qUvbIMsJZkFOnwzv84="
    # print(c.decrypt(base64.b64decode(link), "4a9d9540").replace("\x03", ''))
    # c.get_iplist()
