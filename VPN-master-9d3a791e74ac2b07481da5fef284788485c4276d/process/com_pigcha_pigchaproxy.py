import json
import re

class ComPigchaPigchaproxy:
    def main(self, path):
        res = []
        datas = self.get_data(path)
        for data in datas:
            for bean in json.loads(data):
                if bean["addr"] != "127.0.0.1":
                    res.append({
                                "name": "pigcha加速器",
                                'type': '3',
                                'FQprotocol1': "OTHER",
                                'FQprotocol2': "TCP",
                                'host': bean["addr"],
                                'transfer_protocol': 'TCP',
                                'start_port': bean["port"],
                                'end_port': bean["port"],
                            })
        return res

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [i.strip() for i in datas]


if __name__ == '__main__':
    mxt = ComPigchaPigchaproxy()
    data = mxt.main("../data/data/com_pigcha_pigchaproxy")
    print(data)


