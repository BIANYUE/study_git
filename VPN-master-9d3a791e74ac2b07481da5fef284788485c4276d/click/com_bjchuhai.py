# -*- coding: utf-8 -*-
import binascii
import json
import time
import random
from urllib.parse import urlencode
import binascii
from Crypto.Cipher import DES
import re
from lib.tool import req, wirte_data
from settings import DATA_PATH
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad


# com.bjchuhai 白鲸
class ComGiraffe:
    def __init__(self, app):
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': '139.224.27.183',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.5.0',
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        # 点击切换列表
        datas = self.jiemi(self.get_iplist())
        datas = re.search(r'{.*?}}', datas).group(0)
        json_data = json.loads(datas)
        print(json_data)
        for url, ip_port in json_data['result']['ipNodeMap'].items():
            wirte_data(ip_port + "\n", self.path_name)

    def jiemi(self, data):
        dd = binascii.unhexlify(data)
        key_str = 'google.c'
        mode = DES.MODE_ECB
        decrypted_str = self.des_decrypt(dd, key_str, mode)
        decoded_data = decrypted_str.decode('utf-8')
        # print(decoded_data)
        return decoded_data

    def des_decrypt(self, text, key, mode):
        key_bytes = key.encode('utf-8')
        cipher = DES.new(key_bytes, mode)
        decrypted = cipher.decrypt(text)
        return decrypted

    def get_iplist(self):
        time.sleep(3)
        url = f"http://139.224.27.183/channel/check/y/list?"
        params = {
            'platform': '2',
            'api_version': '14',
            'app_version': '1.45',
            'lang': 'zh',
            '_key': 'de5c6242665492638168',
            'market_id': '1000',
            'pkg': 'com.bjchuhai',
            'device_id': 'rk_4a4ca7e996754f43b7872d7850338fef',
            'model': 'Pixel XL/google',
            'sys_version': '8.1.0',
            'ts': str(int(time.time() * 1000)),
            'sub_pkg': 'com.bjchuhai',
            'version_code': '45',
        }
        url += urlencode(params)
        response = req(url, headers=self.headers, method="post")
        print(response.text)
        return response.text


if __name__ == '__main__':
    app = {
        'appPackage': 'com.bjchuhai',
        'package': 'com.bjchuhai',
        'appActivity': '',
        'click_file': 'com.bjchuhai',
        'process': 'com.bjchuhai',
        'data': 'com.bjchuhai',
        'data_type': 'data',
        'class_name': '',
        'type': 'request',
    }
    cpa = ComGiraffe(app)
    cpa.main()
    # text = "d898d74eadf5bbdb36ce6d311f9584cbf29388500d3667c2387f850c517ead6cdee1a792d5f4248fd2c338064506a20bc422b831ffb04d80baa260432b4f57c619bfb7ae3da174ba1eb6af45f53d76f5472bfdddcdf4711be64ffcc5c461d06b53aed1b765a7707d19bfb7ae3da174ba5a5069d6b4a566c5f79b9ef1a1c13b44b8820d565d3dd85b21403309737707e9c842e378876e6451068f5f9c0e49d68edcfdb0381fa74f253cb910270a4ee7b021403309737707e9d1fb6a42e59c8f9095afa2d8459d926227771b7f4c03e6375c4ac83b2e6b052e9fd96213fbfb8e775e9fc487df922374af1d349e4fe6d9fa90f9e53fa82e755b983fcf655ea0502412a3ea2c96e76894ddd9def9dc09f42be38aefc588d41fdd"
    # t = cpa.decrypt(binascii.unhexlify(text))
    # print(t)
