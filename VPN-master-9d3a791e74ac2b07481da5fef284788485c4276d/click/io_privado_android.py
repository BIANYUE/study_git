# -*- coding: utf-8 -*-
import json
from lib.tool import req, wirte_data
from settings import DATA_PATH


class IoPrivadoAndroid:
    def __init__(self, app):
        self.headers = {
             'User-Agent': 'App-Version: 3.7.564681645; Android-Version: 27',
            # 'Authorization': 'Bearer 4904ff3876b4bb25863b703e263f8762756887c2b6aede0180ef1713',
            'Content-Type': 'application/json',
            #'Host': 'client-api.privado.io',
            'Host': "91.148.229.56",
            'Accept-Encoding': 'gzip',
            'Connection': 'close',
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        self.login()
        data = self.get_iplist()
        print(data)
        wirte_data(json.dumps(data, ensure_ascii=False) + "\n", self.path_name)

    def login(self):
        # url = "https://client-api.privado.io/v1/login"
        url = "https://91.148.229.56/v1/login"

        data = '{"api_key":"9f994c466340e8f2ed60a99396fecb6a","password":"x3IZD54UpEq\u0026","username":"pvvocbew054163"}'
        # data = '{"api_key":"9f994c466340e8f2ed60a99396fecb6a","password":"4Ow?zUG4so9?\u0026","username":"pvmxeqgu921640"}'
        response = req(url, headers=self.headers, data=data, method='post')
        print(response.text + "--------------")

        datas = json.loads(response.text)
        self.headers['Authorization'] = f'Bearer {datas["access_token"]}'

    def get_iplist(self):
        # time.sleep(3)
        # url = f"https://client-api.privado.io/v1/servers?nodes=all"
        url = f"https://91.148.229.56/v1/servers?nodes=all"
        response = req(url, headers=self.headers)
        print(response.text)
        return json.loads(response.text)["servers"]


if __name__ == '__main__':
    app = {
        'appPackage': 'io.privado.android',
        'package': 'io.privado.android',
        'appActivity': '',
        'click_file': 'io_privado_android',
        'process': 'io_privado_android',
        'data': 'io_privado_android',
        'data_type': 'data',
        'class_name': '',
        'type': 'request',
    }
    cpa = IoPrivadoAndroid(app)
    cpa.main()
