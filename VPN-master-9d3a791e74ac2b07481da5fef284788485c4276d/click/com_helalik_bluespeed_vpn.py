# -*- coding: utf-8 -*-
import json

from lib.tool import req, wirte_data
from settings import DATA_PATH


class ComHelalikBluespeedVpn:
    def __init__(self, app):
        self.headers = {
            'x-device-id': 'd9bcb6c046784a14',
            'x-android': '10',
            'x-version-code': '13',
            'x-version': '2.0.0',
            'x-server-id': '',
            'x-d9bcb6c046784a14': '13',
            'user-agent': 'okhttp/3.8.0',
            'accept-encoding': 'gzip',
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        datas = json.loads(self.get_iplist())
        print(datas)
        for data in datas["servers"]:

            wirte_data(data["link"] + "\n", self.path_name)

    def get_iplist(self):
        # time.sleep(3)
        url = f"http://bhsht.top/api/GetServer/alight/HAMARA/IR-MCI"
        response = req(url, headers=self.headers)
        print(response.text)
        return response.text


if __name__ == '__main__':
    app = {
        'appPackage': 'com.helalik.bluespeed.vpn',
        'package': 'com.helalik.bluespeed.vpn',
        'appActivity': '',
        'click_file': 'com_helalik_bluespeed_vpn',
        'process': 'com_helalik_bluespeed_vpn',
        'data': 'com_helalik_bluespeed_vpn',
        'data_type': 'data',
        'class_name': '',
        'type': 'request',
    }
    cpa = ComHelalikBluespeedVpn(app)
    cpa.main()
    # cpa.get_token()
    # a = "ZwYbYfj8LDue90KjL36LJbCL0Q0Pmm1S6CqaG2xWaOL0oqfPpyoFmmhqISgGJr5nhZdCWKKESUSWlJ776AdO4naJ2JUSBp5OZR72IJR/kJiaCq94uFLhc0/ZbE4cOEsGwsdfsPgJJqk9UIVWevVHIQvfI1OFoMUphGLs8iSpcgFqDO9EXiz7XtQg+vwRT6AE8Qlf3JUEThLDS75/aepLiXbIRZ+6BdI3cHZNTQaYBo2xTxpkGJ2ZvsEKBETt2qw6uYxggu+jWCeNc4vImb3OeExaajbes/2jYftAskow0R/QsfkJWcUORZZ3LzmGwIyRDgmPDF8Vlinl8hBIaRz8MkWFnDRUTkplp5ccqKFojk5TQGgbG1EpgzN4Pf6OekTCI9C2rd2eIaW5pEA+uTtSbQL/+NHIL9gClhst/W18Fuhd6ICzofYSZw9m+NAtaazlSNwmUjYCXcIG4R69HDlASnKMfb6hMKCZyaigbl1mm89r+ArRwUthc1AZNdrUjPtBtGSk2wbe9PfFjKmyVoJ+JqiRe4Ih+auzw5E8C9x/gHBgxX5iEk34WHcCmre64D80oPWk4qfy7pB7ngCLk54nZpq/xGUn9ymly6/FzYBF8M5aHezLVr5+GvuOkMKj7wpupQM6lscuull0ez7gqwzxzWxr3A5lpSt7JQcbd5wz+KlNYWZfgayDsd0NkiYcJLOe17IxOChUrFRkR9/hEHozphh5XGMB9BtVs1SjN2luse1UmAxgC9xzJiR/eF7FtKAimRUb6iqTsWVdlixANmZOB8HK4qvoeWhbQzflq8L/5Szc8haEg/1m6l2ytBN4nvRxp7LAXwEF6+6EndXlt5ZDOE+HVI11ZmyFpq6kwasw8m5Hm068YM7isNSjUxrQ42IH+1Nk7dEFfdEHmvLLLUb7B2SffVPLRHnfOtf1nx8AebIAu5ksvEQERCuwcdqNAN1ZVT8ejgJ88QPevmIfBsRfb6Nr0u7YJzJrGXjxHlVNhnJAwkEx5FTsuysgM0YXCnDu0BnP5KOJJo0PXc9mLNgnfShvvZQvl2XUvWRDT4JtuZIKNdUEiYOhhkOJrWCoZ6/7"
    # b = cpa.decrypt(base64.b64decode(a), "MLRzB6w+wYF5tbXD")
    # print(b.encode())
#     b'{"encode_s\x19f#sQ^384686e13b90b0ac4774396c8811e84b","imei":"352530083181883","refresh_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyZXNwb25zZV90eHQiOiIiLCJ1aWQiOjIwMjk4MDgsInVzZXJuYW1lIjoiYmlhbnl1ZSIsInZpcF9sZXZlbCI6MCwidmFsaWRhdGVfdGltZSI6MCwiZnJlZV92YWxpZGF0ZV90aW1lIjoxNjgzMjczMDkwLCJnYW1lX3ZhbGlkYXRlX3RpbWUiOjE2ODIxMjYxNDcsIm1vYmlsZSI6IiIsImVtYWlsIjoiIiwibW9iaWxlX2NvZGUiOiIiLCJkZXZpY2VfbmFtZSI6Imdvb2dsZTpQaXhlbCBYTCIsInNoYXJlX2NvZGUiOiJMUHA3aGgiLCJzaGFyZV91cmwiOiJodHRwczpcL1wvbGIuc3phY3Rpb24uY2NcL2FnZW50XC9zaGFyZV9jb2RlX2luZGV4Lmh0bWw_c2hhcmVfY29kZT1MUHA3aGgiLCJmcmVlX3RpbWVfaW1laSI6IjM1MjUzMDA4MjQ4Nzc5NCIsInZfbGV2ZWwiOjAsInVzZV9mcmVlX3NlcnZpY2UiOjAsImltZWkiOiIzNTI1MzAwODMxODE4ODMiLCJpYXQiOjE2ODM3ODc2ODgsImV4cCI6MTY4ODk3MTY4OH0.w9Dy5mIK7X9hxwCeRgXaP1pJD32na5J6lFRNSK0a6fc","timestamp":"1686637911708"}'
#     b'{"encode_s\x1aa*qTVa4ed8189b02e012bf3164d4542b04cc3","imei":"352530083181883","refresh_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyZXNwb25zZV90eHQiOiIiLCJ1aWQiOjIwMjk4MDgsInVzZXJuYW1lIjoiYmlhbnl1ZSIsInZpcF9sZXZlbCI6MCwidmFsaWRhdGVfdGltZSI6MCwiZnJlZV92YWxpZGF0ZV90aW1lIjoxNjgzMjczMDkwLCJnYW1lX3ZhbGlkYXRlX3RpbWUiOjE2ODIxMjYxNDcsIm1vYmlsZSI6IiIsImVtYWlsIjoiIiwibW9iaWxlX2NvZGUiOiIiLCJkZXZpY2VfbmFtZSI6Imdvb2dsZTpQaXhlbCBYTCIsInNoYXJlX2NvZGUiOiJMUHA3aGgiLCJzaGFyZV91cmwiOiJodHRwczpcL1wvbGIuc3phY3Rpb24uY2NcL2FnZW50XC9zaGFyZV9jb2RlX2luZGV4Lmh0bWw_c2hhcmVfY29kZT1MUHA3aGgiLCJmcmVlX3RpbWVfaW1laSI6IjM1MjUzMDA4MjQ4Nzc5NCIsInZfbGV2ZWwiOjAsInVzZV9mcmVlX3NlcnZpY2UiOjAsImltZWkiOiIzNTI1MzAwODMxODE4ODMiLCJpYXQiOjE2ODM3ODc2ODgsImV4cCI6MTY4ODk3MTY4OH0.w9Dy5mIK7X9hxwCeRgXaP1pJD32na5J6lFRNSK0a6fc","timestamp":"1686637264252"}\x02\x02'
