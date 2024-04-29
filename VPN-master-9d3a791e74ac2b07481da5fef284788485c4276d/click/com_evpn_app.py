# -*- coding: utf-8 -*-
import base64
import json
from Crypto.Cipher import AES
from lib.tool import req, wirte_data
from settings import DATA_PATH


class ComEvpnApp:
    def __init__(self, app):
        self.headers = {
            'Authorization': 'Bearer 1664170097067311104.1ebfb010-4f33-ff74-4cae-986657e5bd88',
            'countryCode': 'CN',
            'country': 'China',
            'region': 'Shanghai',
            'isp': 'CHINANET-SH',
            'referrer': 'googlePlay',
            'device': '{"appVersionCode":25,"appVersionName":"1.1.9","brand":"google","deviceCountry":"CN","deviceName":"marlin","language":"zh","model":"Pixel XL","osName":"Android","osType":"Android","osVersion":"8.1.0","simCode":"","uuid":"34:30:34:45:33:36:31:45:34:39:38:30:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00"}',
            'Content-Type': 'application/json; charset=UTF-8',
            'Host': 'www.elinkapi.info',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/4.10.0',
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        data = self.get_iplist()
        print(data)
        wirte_data(json.dumps(data, ensure_ascii=False) + "\n", self.path_name)

    def get_iplist(self):
        # time.sleep(3)
        url = f"https://www.elinkapi.info/v2/vpn/group/list"
        response = req(url, headers=self.headers, data={}, method='post')
        print(response.text)
        return json.loads(response.text)["data"]["list"]


if __name__ == '__main__':
    app = {
        'appPackage': 'com.evpn.app',
        'package': 'com.evpn.app',
        'appActivity': '',
        'click_file': 'com_evpn_app',
        'process': 'com_evpn_app',
        'data': 'com_evpn_app',
        'data_type': 'data',
        'class_name': '',
        'type': 'request',
    }
    cpa = ComEvpnApp(app)
    cpa.main()
