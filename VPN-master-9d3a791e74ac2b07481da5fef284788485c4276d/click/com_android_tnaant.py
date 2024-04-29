# -*- coding: utf-8 -*-
import base64
import binascii
import hashlib
import json
import random
import time
from urllib.parse import urlencode

from Crypto.Cipher import AES

from lib.tool import req, wirte_data
from settings import DATA_PATH


class ComAndroidTnaant:
    def __init__(self, app):
        self.headers = {
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; Pixel XL Build/OPM4.171019.021.P1) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Host': 'ant.hyysapi.com',
            'Host': 'antapi3.ymjxopa.com',
            'Accept-Encoding': 'gzip',
            'Connection': 'keep-alive',
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        datas = json.loads(self.get_iplist())["data"]
        iv = binascii.unhexlify(datas[:32].lower())
        text = binascii.unhexlify(datas[32:].lower())
        data = json.loads(self.decrypt(iv, text))["data"]["servers"]
        print(data)
        wirte_data(json.dumps(data) + "\n", self.path_name)

    def decrypt(self, iv, text):
        key = binascii.unhexlify("b496f831128e4fe1de33f4b7a2c46e0dd4772524a4826fe4486fcc07e3e2b87f")
        cryptos = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
        plain_text = cryptos.decrypt(text)
        return plain_text.decode()

    def encrypt(self, text):
        key = binascii.unhexlify("b496f831128e4fe1de33f4b7a2c46e0dd4772524a4826fe4486fcc07e3e2b87f")
        iv = binascii.unhexlify("6d7e01a3111bf125e1b3e6d8d1964f60")
        cryptos = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
        plain_text = cryptos.encrypt(text.encode())
        return plain_text

    def get_iplist(self):
        # time.sleep(3)
        # url = f"http://ant.hyysapi.com/api.php"
        url = f"http://antapi3.ymjxopa.com/api.php"
        d = '{"oauth_id":"9de5a950cdac7d4f8dcbd8da5439c97c","oauth_type":"android","mod":"index","code":"homePage","version":"2.6.4","app_type":"ss_proxy","language":0,"bundleId":"com.android.tnaant"}'
        d = '{"oauth_id":"9de5a950cdac7d4f8dcbd8da5439c97c","oauth_type":"android","mod":"index","code":"homePage","version":"2.6.4","app_type":"ss_proxy","language":0,"bundleId":"com.android.tnaant"}'
        r = ''.join([str(random.randint(0, 9)) for i in range(0, 16)])
        dd = self.encrypt(r + d).hex().upper()
        data = {
            'appId': 'android',
            'appVersion': '2.1.8',
            'data': dd,
            'timestamp': str(int(time.time())),
        }
        st = urlencode(data) + "2d5f22520633cfd5c44bacc1634a93f2"
        # st = urlencode(data) + "3f5fa63bcb39da8f7fe2c16faa76dcb5"
        s256 = hashlib.sha256(st.encode()).hexdigest()
        sign = hashlib.md5(s256.encode()).hexdigest()
        data.update({'sign': sign})

        response = req(url, headers=self.headers, data=data, method='post')
        print(response.text)
        return response.text


if __name__ == '__main__':
    app = {
        'appPackage': 'com.android.tnaant',
        'package': 'com.android.tnaant',
        'appActivity': '',
        'click_file': 'com_android_tnaant',
        'process': 'com_android_tnaant',
        'data': 'com_android_tnaant',
        'data_type': 'password',
        'class_name': '',
        'type': 'request',
    }
    cpa = ComAndroidTnaant(app)
    cpa.main()
    # cpa.get_token()
    # a = "ZwYbYfj8LDue90KjL36LJbCL0Q0Pmm1S6CqaG2xWaOL0oqfPpyoFmmhqISgGJr5nhZdCWKKESUSWlJ776AdO4naJ2JUSBp5OZR72IJR/kJiaCq94uFLhc0/ZbE4cOEsGwsdfsPgJJqk9UIVWevVHIQvfI1OFoMUphGLs8iSpcgFqDO9EXiz7XtQg+vwRT6AE8Qlf3JUEThLDS75/aepLiXbIRZ+6BdI3cHZNTQaYBo2xTxpkGJ2ZvsEKBETt2qw6uYxggu+jWCeNc4vImb3OeExaajbes/2jYftAskow0R/QsfkJWcUORZZ3LzmGwIyRDgmPDF8Vlinl8hBIaRz8MkWFnDRUTkplp5ccqKFojk5TQGgbG1EpgzN4Pf6OekTCI9C2rd2eIaW5pEA+uTtSbQL/+NHIL9gClhst/W18Fuhd6ICzofYSZw9m+NAtaazlSNwmUjYCXcIG4R69HDlASnKMfb6hMKCZyaigbl1mm89r+ArRwUthc1AZNdrUjPtBtGSk2wbe9PfFjKmyVoJ+JqiRe4Ih+auzw5E8C9x/gHBgxX5iEk34WHcCmre64D80oPWk4qfy7pB7ngCLk54nZpq/xGUn9ymly6/FzYBF8M5aHezLVr5+GvuOkMKj7wpupQM6lscuull0ez7gqwzxzWxr3A5lpSt7JQcbd5wz+KlNYWZfgayDsd0NkiYcJLOe17IxOChUrFRkR9/hEHozphh5XGMB9BtVs1SjN2luse1UmAxgC9xzJiR/eF7FtKAimRUb6iqTsWVdlixANmZOB8HK4qvoeWhbQzflq8L/5Szc8haEg/1m6l2ytBN4nvRxp7LAXwEF6+6EndXlt5ZDOE+HVI11ZmyFpq6kwasw8m5Hm068YM7isNSjUxrQ42IH+1Nk7dEFfdEHmvLLLUb7B2SffVPLRHnfOtf1nx8AebIAu5ksvEQERCuwcdqNAN1ZVT8ejgJ88QPevmIfBsRfb6Nr0u7YJzJrGXjxHlVNhnJAwkEx5FTsuysgM0YXCnDu0BnP5KOJJo0PXc9mLNgnfShvvZQvl2XUvWRDT4JtuZIKNdUEiYOhhkOJrWCoZ6/7"
    # b = cpa.decrypt(base64.b64decode(a), "MLRzB6w+wYF5tbXD")
    # print(b.encode())
#     b'{"encode_s\x19f#sQ^384686e13b90b0ac4774396c8811e84b","imei":"352530083181883","refresh_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyZXNwb25zZV90eHQiOiIiLCJ1aWQiOjIwMjk4MDgsInVzZXJuYW1lIjoiYmlhbnl1ZSIsInZpcF9sZXZlbCI6MCwidmFsaWRhdGVfdGltZSI6MCwiZnJlZV92YWxpZGF0ZV90aW1lIjoxNjgzMjczMDkwLCJnYW1lX3ZhbGlkYXRlX3RpbWUiOjE2ODIxMjYxNDcsIm1vYmlsZSI6IiIsImVtYWlsIjoiIiwibW9iaWxlX2NvZGUiOiIiLCJkZXZpY2VfbmFtZSI6Imdvb2dsZTpQaXhlbCBYTCIsInNoYXJlX2NvZGUiOiJMUHA3aGgiLCJzaGFyZV91cmwiOiJodHRwczpcL1wvbGIuc3phY3Rpb24uY2NcL2FnZW50XC9zaGFyZV9jb2RlX2luZGV4Lmh0bWw_c2hhcmVfY29kZT1MUHA3aGgiLCJmcmVlX3RpbWVfaW1laSI6IjM1MjUzMDA4MjQ4Nzc5NCIsInZfbGV2ZWwiOjAsInVzZV9mcmVlX3NlcnZpY2UiOjAsImltZWkiOiIzNTI1MzAwODMxODE4ODMiLCJpYXQiOjE2ODM3ODc2ODgsImV4cCI6MTY4ODk3MTY4OH0.w9Dy5mIK7X9hxwCeRgXaP1pJD32na5J6lFRNSK0a6fc","timestamp":"1686637911708"}'
#     b'{"encode_s\x1aa*qTVa4ed8189b02e012bf3164d4542b04cc3","imei":"352530083181883","refresh_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyZXNwb25zZV90eHQiOiIiLCJ1aWQiOjIwMjk4MDgsInVzZXJuYW1lIjoiYmlhbnl1ZSIsInZpcF9sZXZlbCI6MCwidmFsaWRhdGVfdGltZSI6MCwiZnJlZV92YWxpZGF0ZV90aW1lIjoxNjgzMjczMDkwLCJnYW1lX3ZhbGlkYXRlX3RpbWUiOjE2ODIxMjYxNDcsIm1vYmlsZSI6IiIsImVtYWlsIjoiIiwibW9iaWxlX2NvZGUiOiIiLCJkZXZpY2VfbmFtZSI6Imdvb2dsZTpQaXhlbCBYTCIsInNoYXJlX2NvZGUiOiJMUHA3aGgiLCJzaGFyZV91cmwiOiJodHRwczpcL1wvbGIuc3phY3Rpb24uY2NcL2FnZW50XC9zaGFyZV9jb2RlX2luZGV4Lmh0bWw_c2hhcmVfY29kZT1MUHA3aGgiLCJmcmVlX3RpbWVfaW1laSI6IjM1MjUzMDA4MjQ4Nzc5NCIsInZfbGV2ZWwiOjAsInVzZV9mcmVlX3NlcnZpY2UiOjAsImltZWkiOiIzNTI1MzAwODMxODE4ODMiLCJpYXQiOjE2ODM3ODc2ODgsImV4cCI6MTY4ODk3MTY4OH0.w9Dy5mIK7X9hxwCeRgXaP1pJD32na5J6lFRNSK0a6fc","timestamp":"1686637264252"}\x02\x02'
