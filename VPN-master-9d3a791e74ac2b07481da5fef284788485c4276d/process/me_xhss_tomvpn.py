import json
import re


class MeXhssTomvpn:
    def main(self, path):
        datas = self.get_data(path)
        res = []
        for data in datas:
            for d in eval(data):
                res.append({
                    "name": "TomVPN",
                    'type': '3',
                    'FQprotocol1': 'OTHER',
                    'FQprotocol2': 'TLS',
                    'host': d["server_domain"],
                    'transfer_protocol': 'TCP',
                    'start_port': "443",
                    'end_port': "443",
                })
        return res

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [eval(i.strip()) for i in datas]


if __name__ == '__main__':
    mxt = MeXhssTomvpn()
    data = mxt.main("../data/data/me_xhss_tomvpn")
    print(data)

