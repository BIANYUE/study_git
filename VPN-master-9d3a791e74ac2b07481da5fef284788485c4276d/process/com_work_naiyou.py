import json
import re


class ComWorkNaiyou:
    def main(self, path):
        res = []
        datas = [json.loads(data)["data"] for data in self.get_data(path)]
        # print(datas)
        for datass in datas:
            for data in datass:
                host = data["host"]
                ip = data.get("ip")
                if not ip:
                    ip = host
                res.append({
            "name": "安卓加速器",
            'type': '3',
            'FQprotocol1': 'TROJAN',
            'FQprotocol2': 'TLS',
            'host': ip,
            'transfer_protocol': 'TCP',
            'start_port': data["port"],
            'end_port': data["port"],
        })
        return res

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [i.strip() for i in datas if len(i) > 100]


if __name__ == '__main__':
    mxt = ComWorkNaiyou()
    data = mxt.main("../data/data/com_work_naiyou")
    print(data)


