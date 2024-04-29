import json
import re
import base64

class ComMmlMyanmarfontdeveloperHello:
    def main(self, path):
        datas = self.get_data(path)
        res = []
        for data in datas:
            data = data.split(' ')
            res.append({
                "name": "HELLOVPN",
                'type': '3',
                'FQprotocol1': 'OPENVPN',
                'FQprotocol2': 'UDP',
                'host': data[1],
                'transfer_protocol': data[3].upper(),  # 传输协议
                'start_port': data[2],
                'end_port': data[2],
            })
        return res

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [i.strip() for i in datas if "remote" in i]


if __name__ == '__main__':
    mxt = ComMmlMyanmarfontdeveloperHello()
    data = mxt.main("../data/data/com_mml_myanmarfontdeveloper_hello")
    print(data)


