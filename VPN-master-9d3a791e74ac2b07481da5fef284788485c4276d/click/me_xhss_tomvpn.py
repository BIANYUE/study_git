# -*- coding: utf-8 -*-
import base64
import json
import time

from lib.tool import req, wirte_data
from settings import DATA_PATH


# me.xhss.tomvpn
class MeXhssTomvpn:
    def __init__(self, app):
        self.headers = {
            'sign': 'me.xhss.tomvpn',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Content-Length': '0',
            # 'Host': 'xiaoha1.toptop233.top',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.11.0',
            'Connection': 'keep-alive',
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])
        self.MMP = {
            10: 'A', 'A': 10, 11: 'B', 'B': 11, 12: 'C', 'C': 12,
            13: 'D', 'D': 13, 14: 'E', 'E': 14, 15: 'F', 'F': 15
        }
        self.urls = [
            "http://android.toptop233.top:8087/v2/tomLineNew",
            "http://en.tomvps.com/v2/tomLineNew",
            "http://app.allfreepn.com/v2/tomLineNew",
            "http://ru.allfreepn.com/v2/tomLineNew",
            "http://xiaoha1.toptop233.top/v2/tomLineNew"
        ]

    def main(self):
        for url in self.urls:
            data = self.get_iplist(url)
            data = base64.b64decode(self.decryptFromHex(data)).decode()
            print(data)
            wirte_data(json.dumps(data) + "\n", self.path_name)

    def decryptFromHex(self, str):
        i = 0
        i2 = 0
        bArr = []
        while i < len(str):
            if str[i] < '0' or str[i] > '9':
                s = self.MMP.get(str[i])
            else:
                s = ord(str[i]) - ord('0')
            s3 = s << 4
            i3 = i + 1
            if str[i3] < '0' or str[i3] > '9':
                s2 = self.MMP.get(str[i3])
            else:
                s2 = ord(str[i3]) - ord('0')
            bArr.append(s3 + s2)
            i += 2
            i2 += 1
        return self.decrypt(bArr)

    def decrypt(self, bArr):
        KEY = [23, 22, 24, 4, 51, 26, 37, 27, 24, 6, 26, 38, 29, 35, 18, 21, 14, 3, 12, 4, 41, 39, 18, 44, 54, 21, 33,
               35, 31, 22, 34, 53, 51, 44, 8, 12, 3, 0, 28, 1, 48, 9, 51, 57, 20, 44, 27, 3, 16, 48]
        SALT = "dfsad@#%$@TDGDF%$#%@#%WFRGFDHJKcvxznmfdsgdfgs2432534fgdf46t"
        length = len(KEY)
        bArr2 = []
        i = 0
        i2 = 0
        while 1:
            iArr = KEY
            if i2 >= len(iArr):
                break
            bArr2.append(SALT[iArr[i2]])
            i2 += 1
        bArr3 = bytearray()
        i3 = 0
        while i < len(bArr):
            bArr3.append(ord(bArr2[i3 % length]) ^ bArr[i])
            i += 1
            i3 += 1
        return bytes(bArr3).decode()

    def get_iplist(self, url):
        # time.sleep(3)
        response = req(url, headers=self.headers, method='post')
        print(response.text)
        return json.loads(response.text)["data"]


if __name__ == '__main__':
    app = {
        'appPackage': 'me.xhss.tomvpn',
        'package': 'me.xhss.tomvpn',
        'appActivity': '',
        'click_file': 'me_xhss_tomvpn',
        'process': 'me_xhss_tomvpn',
        'data': 'me_xhss_tomvpn',
        'data_type': 'data',
        'class_name': '',
        'type': 'request',
    }
    cpa = MeXhssTomvpn(app)
    cpa.main()

