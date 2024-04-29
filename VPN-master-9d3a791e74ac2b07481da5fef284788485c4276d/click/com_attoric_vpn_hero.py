# -*- coding: utf-8 -*-
import json

from lib.tool import req, wirte_data
from settings import DATA_PATH


class ComAttoricVpnHero:
    def __init__(self, app):
        self.headers = {
            'h006': 'com.attoric.vpn.hero',
            'content-length': '0',
            'accept-encoding': 'gzip',
            'user-agent': 'okhttp/4.10.0',
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        datas = json.loads(self.get_iplist())["result"]
        wirte_data(json.dumps(datas, ensure_ascii=False) + "\n", self.path_name)

    def get_iplist(self):
        # time.sleep(3)
        url = f"https://vapi.heroboostmaster.com/app/api/v1/c03/c0001"
        response = req(url, headers=self.headers, method='post')
        print(response.text)
        return response.text


if __name__ == '__main__':
    app = {
        'appPackage': 'com.attoric.vpn.hero',
        'package': 'com.attoric.vpn.hero',
        'appActivity': '',
        'click_file': 'com_attoric_vpn_hero',
        'process': 'com_attoric_vpn_hero',
        'data': 'com_attoric_vpn_hero',
        'data_type': 'data',
        'class_name': '',
        'type': 'request',
    }
    cpa = ComAttoricVpnHero(app)
    cpa.main()
