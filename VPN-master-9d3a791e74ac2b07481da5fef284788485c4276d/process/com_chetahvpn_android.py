import json
import re

class ComChetahvpnAndroid:
    def main(self, path):
        res = []
        datas = self.get_data(path)
        for data in datas:
            dd = json.loads(data)
            for d in dd:
                for i in d["child"]:
                    res.append({
                                "name": "猎豹VPN",
                                'type': '3',
                                'FQprotocol1': 'SS',
                                'FQprotocol2': 'TCP',
                                'host': i["ip"],
                                'transfer_protocol': 'TCP',
                                'start_port': i["port"],
                                'end_port': i["port"],
                            })
        return res

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [i.strip() for i in datas]


if __name__ == '__main__':
    mxt = ComChetahvpnAndroid()
    data = mxt.main("../data/data/com_chetahvpn_android")
    print(data)


