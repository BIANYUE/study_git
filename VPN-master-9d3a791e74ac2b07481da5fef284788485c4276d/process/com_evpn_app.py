import json
import re


class ComEvpnApp:
    def main(self, path):
        res = []
        datas = self.get_data(path)
        for data in datas:
            for nodelist in json.loads(data):
                for v in nodelist["nodeList"]:
                    vpn_line_list = v["vpn_line_list"]
                    if vpn_line_list:
                        for i in vpn_line_list:
                            res.append({
                                    "name": "易连VPN",
                                    'type': '3',
                                    'FQprotocol1': "OTHER",
                                    'FQprotocol2': "TLS",
                                    'host': i["conn_address"],
                                    'transfer_protocol': 'TCP',
                                    'start_port': i["conn_port"],
                                    'end_port': i["conn_port"],
                                })
        return res

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [i.strip() for i in datas]


if __name__ == '__main__':
    mxt = ComEvpnApp()
    data = mxt.main("../data/data/com_evpn_app")
    print(data)


