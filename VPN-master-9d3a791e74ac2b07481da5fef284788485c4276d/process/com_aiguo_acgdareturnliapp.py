import json
import re
import base64

class ComAiguoAcgdareturnliapp:
    def main(self, path):
        datas = self.get_data(path)
        print(datas)
        return [{
            "name": "旋风加速器",
            'type': '3',
            'FQprotocol1': 'VMESS',
            'FQprotocol2': 'TLSWS',
            'host': data["add"],
            'transfer_protocol': 'TCP',  # 传输协议
            'start_port': data["port"],
            'end_port': data["port"],
        } for data in datas]

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [json.loads(base64.b64decode(i.strip().split("//")[1])) for i in datas if "mess" in i]


if __name__ == '__main__':
    mxt = ComAiguoAcgdareturnliapp()
    data = mxt.main("../data/data/com_aiguo_acgdareturnliapp")
    print(data)


