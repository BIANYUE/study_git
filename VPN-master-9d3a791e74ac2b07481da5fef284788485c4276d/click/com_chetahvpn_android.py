# -*- coding: utf-8 -*-
import base64
import hashlib
import json
import random
import re
import time
from urllib.parse import urlencode

from Crypto.Cipher import AES

# com.chetahvpn.android  猎豹VPN
from lib.tool import req, wirte_data
from settings import DATA_PATH


class ComChetahvpnAndroid:
    def __init__(self, app):
        self.headers = {
            'system': '1',
            'channel': 'android-googleplay',
            'imei': '352530083181883',
            'suffix': '834209',
            'lang': 'zh-tw',
            'version': '81',
            'Content-Type': 'application/json; charset=UTF-8',
            'Host': 'lbapi.szaction.cc',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.12.0',
            'Connection': 'keep-alive',
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        self.get_token(self.login())
        datas = json.loads(self.get_iplist())
        data = datas["data"]
        suffix = datas["suffix"]
        iplist = self.decrypt(base64.b64decode(data), f"MLRzB6w+wY{suffix}")
        print(iplist)
        data = json.loads(iplist)["data"]["server_list"]
        print(data)
        wirte_data(json.dumps(data) + "\n", self.path_name)

    def decrypt(self, text, iv):
        key = "!eRT8&^&-v+t-z2vC2fX9p^u2pDCV_Qc".encode('utf-8')
        iv = iv.encode('utf-8')
        cryptos = AES.new(key, AES.MODE_CBC, iv)
        plain_text = cryptos.decrypt(text).decode()
        padding_len = ord(plain_text[len(plain_text) - 1])
        plain_text = plain_text[0:-padding_len]
        return plain_text
        # return plain_text.decode().replace('\x05', '').replace('\x07', '')

    def encrypt(self, text, iv):
        BLOCK_SIZE = 16  # Bytes
        # 数据进行 PKCS5Padding 的填充
        pad = lambda s: (s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE))
        text = pad(str(text))
        key = "!eRT8&^&-v+t-z2vC2fX9p^u2pDCV_Qc".encode('utf-8')
        iv = iv.encode('utf-8')
        cryptos = AES.new(key, AES.MODE_CBC, iv)
        plain_text = cryptos.encrypt(text.encode())
        return base64.b64encode(plain_text).decode()

    def login(self):
        url = "https://api.liebaonet74.com/user/login"
        headers = {
            'system': '1',
            'channel': 'android-googleplay',
            'imei': '352530083181883',
            'suffix': '834209',
            'lang': 'zh-tw',
            'version': '81',
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.12.0',
        }
        timestamp = str(int(time.time() * 1000))
        encode_sign = hashlib.md5(f"device_name=google:Pixel XL&imei=352530083181883&password=BY981018&timestamp={timestamp}&username=bianyue&9_s9f7rduMD6WZ6At-?PT^dbW6!9zzhXXtrr".encode()).hexdigest()
        post_data = {"device_name":"google:Pixel XL","encode_sign":encode_sign,"imei":"352530083181883","password":"BY981018","timestamp":str(timestamp),"username":"bianyue"}
        r = ''.join([str(random.randint(0, 9)) for i in range(6)])
        data = {"post-data": self.encrypt(json.dumps(post_data), f"MLRzB6w+wY{r}")}
        headers["suffix"] = r
        response = req(url, headers=headers, data=json.dumps(data), method="post")
        # print(response.text)
        # print(response.headers)
        data = json.loads(response.text)
        a = self.decrypt(base64.b64decode(data["data"]), f"MLRzB6w+wY{data['suffix']}")
        print(a)
        return json.loads(a)["data"]["refresh_token"]

    def get_token(self, token):
        # token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyZXNwb25zZV90eHQiOiIiLCJ1aWQiOjIwMjk4MDgsInVzZXJuYW1lIjoiYmlhbnl1ZSIsInZpcF9sZXZlbCI6MCwidmFsaWRhdGVfdGltZSI6MCwiZnJlZV92YWxpZGF0ZV90aW1lIjoxNjg1NDk2MzgyLCJnYW1lX3ZhbGlkYXRlX3RpbWUiOjE2ODIxMjYxNDcsIm1vYmlsZSI6IiIsImVtYWlsIjoiIiwibW9iaWxlX2NvZGUiOiIiLCJkZXZpY2VfbmFtZSI6Imdvb2dsZTpQaXhlbCBYTCIsInNoYXJlX2NvZGUiOiJMUHA3aGgiLCJzaGFyZV91cmwiOiJodHRwczpcL1wvbGIuc3phY3Rpb24uY2NcL2FnZW50XC9zaGFyZV9jb2RlX2luZGV4Lmh0bWw_c2hhcmVfY29kZT1MUHA3aGgiLCJmcmVlX3RpbWVfaW1laSI6IjM1MjUzMDA4MjQ4Nzc5NCIsInZfbGV2ZWwiOjAsInVzZV9mcmVlX3NlcnZpY2UiOjAsImltZWkiOiIzNTI1MzAwODMxODE4ODMiLCJpYXQiOjE2ODkxNDI0MTMsImV4cCI6MTY5NDMyNjQxM30.pHSCCFLjrKhJuOrlRSct6Tmd6AsXTeJY991zCmYeqj0"
        imei = "352530083181883"
        timestamp = str(int(time.time() * 1000))
        url = f"https://lbapi.szaction.cc/user/refreshtoken"
        post_data = {"imei": imei, "refresh_token": token, "timestamp": timestamp}
        encode_sign = hashlib.md5((urlencode(post_data) + "&9_s9f7rduMD6WZ6At-?PT^dbW6!9zzhXXtrr").encode()).hexdigest()
        a = '{"encode_sign":"%s","imei":"352530083181883","refresh_token":"%s","timestamp":"%s"}' % (
        encode_sign, token, timestamp)
        r = ''.join([str(random.randint(0, 9)) for i in range(6)])
        data = {"post-data": self.encrypt(a, f"MLRzB6w+wY{r}")}
        # print(data)
        self.headers["suffix"] = r
        response = req(url, headers=self.headers, data=json.dumps(data), method="post")
        # print(response.text)
        data = json.loads(response.text)
        a = self.decrypt(base64.b64decode(data["data"]), f"MLRzB6w+wY{data['suffix']}")
        print(a)
        self.token = re.search('"token":"(.*?)"', a).group(1)

    def get_iplist(self):
        # time.sleep(3)
        url = f"https://lbapi.szaction.cc/index/nodealllist"
        post_data = {"imei": "352530083181883", "timestamp": str(int(time.time() * 1000)),
                     "token": self.token}
        encode_sign = hashlib.md5((urlencode(post_data) + "&9_s9f7rduMD6WZ6At-?PT^dbW6!9zzhXXtrr").encode()).hexdigest()
        post_data.update({"encode_sign": encode_sign})
        data = {"post-data": self.encrypt(json.dumps(post_data), "MLRzB6w+wY834209")}
        # print(data)
        response = req(url, headers=self.headers, data=json.dumps(data), method="post")
        # print(response.text)
        # print(response.headers)
        return response.text


if __name__ == '__main__':
    app = {
        'appPackage': 'com.chetahvpn.android',
        'package': 'com.chetahvpn.android',
        'appActivity': '',
        'click_file': 'com_chetahvpn_android',
        'process': 'com_chetahvpn_android',
        'data': 'com_chetahvpn_android',
        'data_type': 'data',
        'class_name': '',
        'type': 'request',
    }
    cpa = ComChetahvpnAndroid(app)
    cpa.main()
    # cpa.login()
    # a = "ZwYbYfj8LDue90KjL36LJbCL0Q0Pmm1S6CqaG2xWaOL0oqfPpyoFmmhqISgGJr5nhZdCWKKESUSWlJ776AdO4naJ2JUSBp5OZR72IJR/kJiaCq94uFLhc0/ZbE4cOEsGwsdfsPgJJqk9UIVWevVHIQvfI1OFoMUphGLs8iSpcgFqDO9EXiz7XtQg+vwRT6AE8Qlf3JUEThLDS75/aepLiXbIRZ+6BdI3cHZNTQaYBo2xTxpkGJ2ZvsEKBETt2qw6uYxggu+jWCeNc4vImb3OeExaajbes/2jYftAskow0R/QsfkJWcUORZZ3LzmGwIyRDgmPDF8Vlinl8hBIaRz8MkWFnDRUTkplp5ccqKFojk5TQGgbG1EpgzN4Pf6OekTCI9C2rd2eIaW5pEA+uTtSbQL/+NHIL9gClhst/W18Fuhd6ICzofYSZw9m+NAtaazlSNwmUjYCXcIG4R69HDlASnKMfb6hMKCZyaigbl1mm89r+ArRwUthc1AZNdrUjPtBtGSk2wbe9PfFjKmyVoJ+JqiRe4Ih+auzw5E8C9x/gHBgxX5iEk34WHcCmre64D80oPWk4qfy7pB7ngCLk54nZpq/xGUn9ymly6/FzYBF8M5aHezLVr5+GvuOkMKj7wpupQM6lscuull0ez7gqwzxzWxr3A5lpSt7JQcbd5wz+KlNYWZfgayDsd0NkiYcJLOe17IxOChUrFRkR9/hEHozphh5XGMB9BtVs1SjN2luse1UmAxgC9xzJiR/eF7FtKAimRUb6iqTsWVdlixANmZOB8HK4qvoeWhbQzflq8L/5Szc8haEg/1m6l2ytBN4nvRxp7LAXwEF6+6EndXlt5ZDOE+HVI11ZmyFpq6kwasw8m5Hm068YM7isNSjUxrQ42IH+1Nk7dEFfdEHmvLLLUb7B2SffVPLRHnfOtf1nx8AebIAu5ksvEQERCuwcdqNAN1ZVT8ejgJ88QPevmIfBsRfb6Nr0u7YJzJrGXjxHlVNhnJAwkEx5FTsuysgM0YXCnDu0BnP5KOJJo0PXc9mLNgnfShvvZQvl2XUvWRDT4JtuZIKNdUEiYOhhkOJrWCoZ6/7"
    # b = cpa.decrypt(base64.b64decode(a), "MLRzB6w+wYF5tbXD")
    # print(b.encode())
#     b'{"encode_s\x19f#sQ^384686e13b90b0ac4774396c8811e84b","imei":"352530083181883","refresh_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyZXNwb25zZV90eHQiOiIiLCJ1aWQiOjIwMjk4MDgsInVzZXJuYW1lIjoiYmlhbnl1ZSIsInZpcF9sZXZlbCI6MCwidmFsaWRhdGVfdGltZSI6MCwiZnJlZV92YWxpZGF0ZV90aW1lIjoxNjgzMjczMDkwLCJnYW1lX3ZhbGlkYXRlX3RpbWUiOjE2ODIxMjYxNDcsIm1vYmlsZSI6IiIsImVtYWlsIjoiIiwibW9iaWxlX2NvZGUiOiIiLCJkZXZpY2VfbmFtZSI6Imdvb2dsZTpQaXhlbCBYTCIsInNoYXJlX2NvZGUiOiJMUHA3aGgiLCJzaGFyZV91cmwiOiJodHRwczpcL1wvbGIuc3phY3Rpb24uY2NcL2FnZW50XC9zaGFyZV9jb2RlX2luZGV4Lmh0bWw_c2hhcmVfY29kZT1MUHA3aGgiLCJmcmVlX3RpbWVfaW1laSI6IjM1MjUzMDA4MjQ4Nzc5NCIsInZfbGV2ZWwiOjAsInVzZV9mcmVlX3NlcnZpY2UiOjAsImltZWkiOiIzNTI1MzAwODMxODE4ODMiLCJpYXQiOjE2ODM3ODc2ODgsImV4cCI6MTY4ODk3MTY4OH0.w9Dy5mIK7X9hxwCeRgXaP1pJD32na5J6lFRNSK0a6fc","timestamp":"1686637911708"}'
#     b'{"encode_s\x1aa*qTVa4ed8189b02e012bf3164d4542b04cc3","imei":"352530083181883","refresh_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyZXNwb25zZV90eHQiOiIiLCJ1aWQiOjIwMjk4MDgsInVzZXJuYW1lIjoiYmlhbnl1ZSIsInZpcF9sZXZlbCI6MCwidmFsaWRhdGVfdGltZSI6MCwiZnJlZV92YWxpZGF0ZV90aW1lIjoxNjgzMjczMDkwLCJnYW1lX3ZhbGlkYXRlX3RpbWUiOjE2ODIxMjYxNDcsIm1vYmlsZSI6IiIsImVtYWlsIjoiIiwibW9iaWxlX2NvZGUiOiIiLCJkZXZpY2VfbmFtZSI6Imdvb2dsZTpQaXhlbCBYTCIsInNoYXJlX2NvZGUiOiJMUHA3aGgiLCJzaGFyZV91cmwiOiJodHRwczpcL1wvbGIuc3phY3Rpb24uY2NcL2FnZW50XC9zaGFyZV9jb2RlX2luZGV4Lmh0bWw_c2hhcmVfY29kZT1MUHA3aGgiLCJmcmVlX3RpbWVfaW1laSI6IjM1MjUzMDA4MjQ4Nzc5NCIsInZfbGV2ZWwiOjAsInVzZV9mcmVlX3NlcnZpY2UiOjAsImltZWkiOiIzNTI1MzAwODMxODE4ODMiLCJpYXQiOjE2ODM3ODc2ODgsImV4cCI6MTY4ODk3MTY4OH0.w9Dy5mIK7X9hxwCeRgXaP1pJD32na5J6lFRNSK0a6fc","timestamp":"1686637264252"}\x02\x02'
