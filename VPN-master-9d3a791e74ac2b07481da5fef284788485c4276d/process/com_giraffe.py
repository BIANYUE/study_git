import json
import re


class ComGiraffe:
    def main(self, path):
        datas = self.get_data(path)

        return [{
            "name": "安易加速器",
            'type': '3',
            'FQprotocol1': 'OTHER',
            'FQprotocol2': 'WS',
            'host': data.split(':')[0],
            'transfer_protocol': 'TCP',  # 传输协议
            'start_port': data.split(':')[1],
            'end_port': data.split(':')[1],
        } for data in datas]

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [i.strip() for i in datas]


if __name__ == '__main__':
    mxt = ComGiraffe()
    data = mxt.main("../data/data/com_giraffe")
    print(data)


