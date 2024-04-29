import json
import time

import requests
import urllib3
from Crypto.Cipher import AES
import base64

from lib.tool import wirte_data, req
from settings import DATA_PATH

urllib3.disable_warnings()


class ComAiguoAcgdareturnliapp:
    def __init__(self, app):
        self.token = ''
        self.headers = {
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; Pixel XL Build/OPM4.171019.021.P1)',
            'Host': 'www.xch8kf.xyz:20000',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])
        self.get_token()

    def main(self):
        for n in range(5):
            iplist = self.get_iplist()["res"]
            for ip in iplist:
                for i in ip["data"]:
                    area = i["id"]
                    self.get_ipinfo(area)

    def decrypt(self, text):
        key = "awdtif20190619ti".encode('utf-8')
        iv = "awdtif20190619ti".encode('utf-8')
        mode = AES.MODE_CBC
        cryptos = AES.new(key, mode, iv)
        plain_text = cryptos.decrypt(text).decode()
        # padding_len = ord(plain_text[len(plain_text) - 1])
        # plain_text = plain_text[0:-padding_len]
        # print(plain_text)
        return plain_text

    def get_token(self):
        url = "https://www.xgrjjf.xyz:20000/myapi/eapilogin?&vip=false&proto=v4&platform=android&ver=8.1.0&deviceid=82a84d2256c91f66unknown&unicode=82a84d2256c91f66unknown&t=1685246144864&code=6LBQQ0K&recomm_code=&f=2023-05-27&install=2023-05-27&token=&package=com.aiguo.acgdareturnliapp&width=360.0&height=755.0&w=1080&h=2340&apps=67a3b2ec708d5467af4f959b23a278b3&phone=wenfufa@hotmail.com&passwd=zhanghao2022&ver_code=&sign=9bc87b511851d4380cbf9fe733b4bdf9"
        response = req(url, headers=self.headers)
        print(response.text)
        self.token = json.loads(self.decrypt(base64.b64decode(response.text)).replace('\x00', ''))["token"]

    def get_iplist(self):
        url = f"https://www.xgrjjf.xyz:20000/myapi/apinodelist?level=2&vip=true&proto=v4&platform=android&ver=8.1.0&deviceid=82a84d2256c91f66unknown&unicode=82a84d2256c91f66unknown&t=1685241897448&code=6LBQQ0K&recomm_code=&f=2023-05-27&install=2023-05-27&token={self.token}&package=com.aiguo.acgdareturnliapp&width=360.0&height=755.0&w=1080&h=2340&apps=67a3b2ec708d5467af4f959b23a278b3"
        response = req(url, headers=self.headers)
        return json.loads(response.text)

    def get_ipinfo(self, area):
        time.sleep(3)
        url = f"https://www.xgrjjf.xyz:20000/api/evmess?&vip=true&proto=v4&platform=android&ver=8.1.0&deviceid=82a84d2256c91f66unknown&unicode=82a84d2256c91f66unknown&t=1685242639925&code=6LBQQ0K&recomm_code=&f=2023-05-27&install=2023-05-27&token={self.token}&package=com.aiguo.acgdareturnliapp&width=360.0&height=755.0&w=1080&h=2340&apps=67a3b2ec708d5467af4f959b23a278b3&area={area}"
        response = req(url, headers=self.headers)
        data = self.decrypt(base64.b64decode(response.text)).replace('\x00', '')
        print(data)
        wirte_data(data + "\n", self.path_name)


if __name__ == '__main__':
    app = {
        'appPackage': 'com.aiguo.acgdareturnliapp',
        'package': 'com.aiguo.acgdareturnliapp',
        'appActivity': '',
        'click_file': 'com_aiguo_acgdareturnliapp',
        'process': 'com_aiguo_acgdareturnliapp',
        'data': 'com_aiguo_acgdareturnliapp',
        'data_type': 'data',
        'class_name': '',
        'type': 'request',
    }
    c = ComAiguoAcgdareturnliapp(app)
    c.main()
