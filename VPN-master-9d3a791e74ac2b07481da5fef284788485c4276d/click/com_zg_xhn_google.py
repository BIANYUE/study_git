import json
import time

import requests
import urllib3
from Crypto.Cipher import AES
import base64

from lib.tool import wirte_data, req
from settings import DATA_PATH

urllib3.disable_warnings()


class ComZgXhnGoogle:
    def __init__(self, app):
        self.headers = {
            'Authorization': 'e9ed368f4c60bec7c0fd024b876bd764',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '309',
            'Host': 'ltzproxy.zhxcshop.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/4.9.2',
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        iplist = self.get_iplist()
        # print(iplist)
        l = []
        for data in iplist["data"]:
            d = {
                "server_ip": self.decrypt(base64.b64decode(data["server_ip"])),
                "server_port": self.decrypt(base64.b64decode(data["server_port"])),
                "server_pwd": self.decrypt(base64.b64decode(data["server_pwd"])),
                "encryption": self.decrypt(base64.b64decode(data["encryption"])),
                "protocol": self.decrypt(base64.b64decode(data["protocol"])),
                "protocol_param": self.decrypt(base64.b64decode(data["protocol_param"])),
                "obfs": self.decrypt(base64.b64decode(data["obfs"])),
                "obfs_param": self.decrypt(base64.b64decode(data["obfs_param"]))
            }
            l.append(d)
        print(l)
        wirte_data(json.dumps(l) + "\n", self.path_name)

    def decrypt(self, text):
        key = "vpfjnxmftyisebts".encode('utf-8')
        iv = "ftONwyJtvpsysWpM".encode('utf-8')
        mode = AES.MODE_CBC
        cryptos = AES.new(key, mode, iv)
        plain_text = cryptos.decrypt(text)
        return plain_text.decode().replace('\x0e', '').replace('\x0c', '').replace('\x10', '').replace('\x05', '').replace('\x0b', '').replace('\x08', '').replace('\x02', '').replace('\x03', '')

    def get_iplist(self):
        # time.sleep(3)
        url = f"https://ltzproxy.zhxcshop.com/api/v2/get_node_server"
        data = {
            'user_id': '4824187',
            'platform': '1',
            'app_name': 'bluerabbit',
            'app_version': '040305',
            'device_id': 'f8dcc64e69c3c133751d4bf3784317e68122',
            'udid': 'f8dcc64e69c3c133751d4bf3784317e68122',
            'channel_type': '1',
            'device_name': 'Pixel XL',
            'vendor': 'google',
            'extend_source': '211',
            'package': 'com.zg.xhn.google',
            'timestamp': '1685932795',
            'sign': '99c967f634120a4b0a4ad5a71cd6817e',
        }
        response = req(url, headers=self.headers, data=data, method="post")
        # print(response.text)
        return json.loads(response.text)


if __name__ == '__main__':
    app = {
        'appPackage': 'com.zg.xhn.google',
        'package': 'com.zg.xhn.google',
        'appActivity': '',
        'click_file': 'com_zg_xhn_google',
        'process': 'com_zg_xhn_google',
        'data': 'com_zg_xhn_google',
        'data_type': 'password',
        'class_name': '',
        'type': 'request',
    }
    c = ComZgXhnGoogle(app)
    # d = c.decrypt(base64.b64decode("Jo28JKEhznEnAMCi5y9Phg=="))
    # print(d)
    c.main()
