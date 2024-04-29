# # -*- coding: utf-8 -*-
import base64
import json
from Crypto.Cipher import AES
from lib.tool import req, wirte_data
from settings import DATA_PATH
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import binascii
import re
import datetime
#
#
class ComEvpnApp:
    def __init__(self, app):
        self.headers = {
            'user-agent': "Mozilla/5.0 (Linux; Android 8.1.0; Pixel XL Build/OPM4.171019.021.P1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.143 Mobile Safari/537.36",
            'content-type': 'application/x-www-form-urlencoded',
            'accept-encoding': 'gzip'
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        datas = self.jiemi(self.get_iplist())
        # print(datas)
        datas = re.search(r"\{(?:[^{}]*\{[^{}]*\}[^{}]*|[^{}]*)*\}", datas).group()
        # print(datas)
        json_data = json.loads(datas)
        print(json_data['goserverlist'])
        for ip_port in json_data['goserverlist']:
            wirte_data(str(ip_port) + "\n", self.path_name)

    def jiemi(self, data):
        key = "UDRnpNG4zVafoPDyKirGyqnq0gP4wlnS"
        return self.aes_decrypt_hex(data, key)

    def aes_decrypt_hex(self, ciphertext_hex, key):
        def hex_to_bytes(hex_string):
            return binascii.unhexlify(hex_string)

        ciphertext = hex_to_bytes(ciphertext_hex)
        key_bytes = key.encode('utf-8')
        backend = default_backend()
        cipher = Cipher(algorithms.AES(key_bytes), modes.ECB(), backend=backend)
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        return plaintext.decode('utf-8')



    def get_iplist(self):
        # time.sleep(3)
        url = f"https://edgeapi.mmasafe.com/node/getInformation_ex"

        current_time = datetime.datetime.now()

        # 将当前时间格式化为指定的时间格式
        formatted_time = current_time.strftime("%Y年%m月%d日%H:%M:%S")
        data = {
            't' : formatted_time,
            'value': '47F391C374463A96EC9E8D79C31C67210704AEA7610A9333749CFE65C97FB242A89162A7AD022381CEB788445FE141349A5FFB021852AA75B9C8E5B87F317776026658C35E24F8A681C07A06F7285DD908A0FE3688F06FE0569BDFAF0F0E27CC189903C8F09ECACE990A449F92314F9C642E29DABECA036F6BD2CECD5C5BB8B9A32901556CD4E20F046645839F55A939F9204BC066FA72B70490DABBCD5512350C1D2C22BB229A562E98A143C670396F'
        }
        response = req(url, headers=self.headers, data=data, method='post')
        print(response.text)
        return json.loads(response.text)["data"]


if __name__ == '__main__':
    app = {
        'appPackage': 'com.tube.client',
        'package': 'com.tube.client',
        'appActivity': '',
        'click_file': 'com_tube_client',
        'process': 'com_tube_client',
        'data': 'com_tube_client',
        'data_type': 'data',
        'class_name': '',
        'type': 'request',
    }
    cpa = ComEvpnApp(app)
    cpa.main()

