import json
import re


class ComLeitingLt401:
    def main(self, path):
        datas = self.get_data(path)

        return [{
            "name": "雷霆加速器",
            'type': '3',
            'FQprotocol1': 'OTHER',
            'FQprotocol2': 'TLSWS',
            'host': data["add"],
            'transfer_protocol': 'TCP',  # 传输协议
            'start_port': data["port"],
            'end_port': data["port"],
        } for data in datas]

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [json.loads(i.strip()) for i in datas if len(i) > 10]


if __name__ == '__main__':
    mxt = ComLeitingLt401()
    data = mxt.main("../data/data/com_leiting_lt401")
    print(data)
