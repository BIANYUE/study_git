# -*- coding: utf-8 -*-
import base64
import json
from Crypto.Cipher import AES
from lib.tool import req, wirte_data
from settings import DATA_PATH


class ComPigchaPigchaproxy:
    def __init__(self, app):
        self.headers = {
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; Pixel XL Build/OPM4.171019.021.P1)',
            # 'Host': '124.221.200.204:8082',
            'Host': '124.221.218.32: 8089',
            'Accept-Encoding': 'gzip',
            'Connection': 'keep-alive',
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        data = self.decrypt(base64.b64decode(self.get_iplist()))
        print(data)
        wirte_data(data + "\n", self.path_name)

    def decrypt(self, text):
        key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx".encode('utf-8')
        iv = "xxxxxxxxxxxxxxxx".encode('utf-8')
        cryptos = AES.new(key, AES.MODE_CBC, iv)
        plain_text = cryptos.decrypt(text).decode()
        padding_len = ord(plain_text[len(plain_text) - 1])
        plain_text = plain_text[0:-padding_len]
        return plain_text

    def get_iplist(self):
        # time.sleep(3)
        # url = f"http://124.221.200.204:8082/v3/sys/clientnodelist?email=1148421588@qq.com&platform=android&cur_version=5270416"
        url = f"http://124.221.218.32:8089/v3/sys/clientnodelist?email=2684726009@qq.com&platform=android&cur_version=5270416"
        response = req(url, headers=self.headers)
        print(response.text)
        return json.loads(response.text)["data"]


if __name__ == '__main__':
    app = {
        'appPackage': 'com.pigcha.pigchaproxy',
        'package': 'com.pigcha.pigchaproxy',
        'appActivity': '',
        'click_file': 'com_pigcha_pigchaproxy',
        'process': 'com_pigcha_pigchaproxy',
        'data': 'com_pigcha_pigchaproxy',
        'data_type': 'data',
        'class_name': '',
        'type': 'request',
    }
    cpa = ComPigchaPigchaproxy(app)
    cpa.main()

