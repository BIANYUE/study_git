import json
import re


class IoPrivadoAndroid:
    def main(self, path):
        res = []
        datas = self.get_data(path)
        for data in datas:
            for servers in json.loads(data):
                for i in servers["protocols"]:
                    if i["port"] != 0:
                        res.append({
                                "name": "PrivadoVPN",
                                'type': '3',
                                'FQprotocol1': "OPENVPN",
                                'FQprotocol2': i["protocol"],
                                'host': servers["ip_address"],
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
    mxt = IoPrivadoAndroid()
    data = mxt.main("../data/data/io_privado_android")
    print(data)


