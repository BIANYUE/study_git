# -*- coding: utf-8 -*-
import binascii
import json
import time
import random
from urllib.parse import urlencode

from Crypto.Cipher import DES

from lib.tool import req, wirte_data
from settings import DATA_PATH


# com.giraffe 安易加速器
class ComGiraffe:
    def __init__(self, app):
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': "0",
            # "Content-Length": "0",
            'Host': 'z1.goofficez.com',
            # 'Host': '47.103.138.200',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.5.0',
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        # 点击切换列表
        datas = self.jiemi(self.get_iplist())
        # print(datas)
        for i in datas["result"]["regions"]:
            print(i)
            if i["lockedTip"] == '':
                id = i["id"]
                noteid_dict = self.jiemi(self.get_node_id(id))["result"]["nodes"]
                for k in noteid_dict:
                    print(k)
                    ipinfo = self.jiemi(self.get_ipinfo(id, k))["result"]["outboundIpPorts"]
                    print(ipinfo)
                    if ipinfo:
                        wirte_data(ipinfo + "\n", self.path_name)

    def jiemi(self, data):
        dd = self.decrypt(binascii.unhexlify(data))
        # print(json.loads(dd))
        return json.loads(dd)

    def decrypt(self, text):
        cryptos = DES.new("microsof".encode('utf-8'), DES.MODE_ECB)
        decrypted_bytes = cryptos.decrypt(text)
        # print(decrypted_bytes)
        plain_text = cryptos.decrypt(text).decode()
        for i in ['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\x09', '\x0a', '\x0b', '\x0c', '\x0d', '\x0e', '\x0f']:
            plain_text = plain_text.replace(i, '')
        return plain_text

    def get_ipinfo(self, i, noteid):
        url = f"https://z1.goofficez.com/v1/node/config/get?"
        # url = f"http://47.103.138.200/v1/node/config/get?"

        params = {
            'platform': '2',
            'api_version': '14',
            'app_version': '1.1',
            'lang': 'zh',
            # '_key': 'emSbTYOsEb0kpJe5rXHqZ32S_oudwIgo',
            # '_key' : '1vInePm7GxD1RBVELfbL-42yjDvS4UB-',
            '_key': 'pNn9B9t8f7J6tz0w7WJAbjsiJzqkdMFy',
            'market_id': '1000',
            'pkg': 'com.giraffe',
            # 'device_id': 'rk_da7e29ef07bc4bcbaa81b3962956c511',
            'device_id': 'rk_4a4ca7e996754f43b7872d7850338fef',
            # 'model': 'Pixel%20XL/google',
            'model': 'Pixel XL/google',
            'sys_version': '8.1.0',
            'ts': str(int(time.time() * 1000)),
            'sub_pkg': 'com.giraffe',
            'version_code': '2',
        }
        data = {'load_time': str(random.randint(500, 1000)), 'region_id': i, 'node_id': noteid}
        url += urlencode(params)
        response = req(url, headers=self.headers, data=data, method="post")
        print(response.text)
        return response.text

    def get_node_id(self, i):
        url = f"https://z1.goofficez.com/v1/node/list?"
        # url = f"http://47.103.138.200/v1/node/list?"
        params = {
            'platform': '2',
            'api_version': '14',
            'app_version': '1.1',
            'lang': 'zh',
            # '_key': 'emSbTYOsEb0kpJe5rXHqZ32S_oudwIgo',
            # '_key': '1vInePm7GxD1RBVELfbL-42yjDvS4UB-',
            '_key': 'pNn9B9t8f7J6tz0w7WJAbjsiJzqkdMFy',
            'market_id': '1000',
            'pkg': 'com.giraffe',
            # 'device_id': 'rk_da7e29ef07bc4bcbaa81b3962956c511',
            'device_id': 'rk_4a4ca7e996754f43b7872d7850338fef',
            'model': 'Pixel XL/google',
            'sys_version': '8.1.0',
            'ts': str(int(time.time() * 1000)),
            'sub_pkg': 'com.giraffe',
            'version_code': '2',
        }
        data = {"region_id": i}
        url += urlencode(params)
        response = req(url, headers=self.headers, data=data, method="post")
        # print(response.text)
        return response.text

    def get_iplist(self):
        # time.sleep(3)
        url = f"https://z1.goofficez.com/v1/region/list?"
        # url = f"http://47.103.138.200/v1/region/list?"
        params = {
            'platform': '2',
            'api_version': '14',
            'app_version': '1.1',
            'lang': 'zh',
            # '_key': 'emSbTYOsEb0kpJe5rXHqZ32S_oudwIgo',
            # '_key': '1vInePm7GxD1RBVELfbL-42yjDvS4UB-',
            '_key': 'pNn9B9t8f7J6tz0w7WJAbjsiJzqkdMFy',
            'market_id': '1000',
            'pkg': 'com.giraffe',
            # 'device_id': 'rk_da7e29ef07bc4bcbaa81b3962956c511',
           # 'device_id': 'rk_4a4ca7e996754f43b7872d7850338fef',
            'device_id': 'rk_4a4ca7e996754f43b7872d7850338fef',
            'model': 'Pixel XL/google',
            'sys_version': '8.1.0',
            'ts': str(int(time.time() * 1000)),
            'sub_pkg': 'com.giraffe',
            'version_code': '2',
        }

        url += urlencode(params)
        response = req(url, headers=self.headers, method="post")
        print(response.text)
        return response.text


if __name__ == '__main__':
    app = {
        'appPackage': 'com.giraffe',
        'package': 'com.giraffe',
        'appActivity': '',
        'click_file': 'com_giraffe',
        'process': 'com_giraffe',
        'data': 'com_giraffe',
        'data_type': 'data',
        'class_name': '',
        'type': 'request',
    }
    cpa = ComGiraffe(app)
    cpa.main()
    # text = "66e8ffac2a196ccd777f63cb1c0590c694d4ac4092227d161d9561ca2330fd5f7128b41db9c7efecc1686c797c84a3965d9429ce9a3d4bf384256057bfd779513776af529e5d6b594246b8efca4e246d617211b138f4ab4547a1053c86ae7ec294fcc999d508137db7178f49af7bf3ab783d03bcacf3f3f0df561d356314f449e53da81901e8793ec9ea174a047ff0181dd7c788c2aea32dfd91bb26f6cf0921a98378b88a1d14ab6a5df63b00de18465f9384f282ff276e51270e598858248a9a0308b14c301b5002839bad5cf5d052b3b06adf4a7c4b0d567b9eb9797b475ad22344715118f0623b371ea3e1cc24d3a60ad7e1ab2124708264747eed9f7efc054214c93e0777e0a62f95d37101acb296d44b44fccfdaeabfe80dba29ef07c1662469957fd75da23954e31cd59ae1930be5e2025cb5115c3bb4a5aea11ba3d3fa8cc4bf2f2280f1608f7c0373a8ba87f0bde42d067f9c5cb9b7eabcab7ef53899ac37a865e37eacd2f6afaecc77d69f80b65dd4b1edeed005e62881569e85ac446ab4c2d3838a937f9304d82cdb3283362e827488768f2e3ae1ce17575c82e1fa8cc4bf2f2280f13c56a222f72e3b159ea034f89423b47dce01fe47cec19abb6735870372478524a94e3e1705b851799f69b50a0b30986723ef8332f48e4787e5eccdd8fa9fc28e28b51309be546cd3f731e109c3947b1cc3feb3a20f16e4e6082f9a3d14f33ebcadaf34fb1007b45961a68f61a0c507b5fb079692281aca13389e5ad6152444eaedfbebbd1e77889118ee0cfe46ef234449e37b4ea9faf55dafe34c5739b9bed1c04b74eeeb6fa86ef2b6b41872530a3067ac0008a85dade10f5dba9b049d48c73389ccf3922ff61faad74cb9bd17d27bc25bae9ba0cebbdf30708a1eda065f5e45f7e33bdec31bc13460435069cb122afb28fff76f7921840267aa23900227ebd50ef103047c0d7f099511a4ad9f4b06521071dcea915505"
    # t = cpa.decrypt(binascii.unhexlify(text))
    # print(t)
