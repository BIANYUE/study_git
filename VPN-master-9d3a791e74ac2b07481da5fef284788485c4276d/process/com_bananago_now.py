import json
import re

class ComBananagoNow:
    def main(self, path):
        res = []
        datas = self.get_data(path)
        for data in datas:
            type = re.search("type: (.*?),", data).group(1)
            if type == "ssr":
                f1 = "SS"
                t = "SSR"
            else:
                f1 = "TROJAN"
                t = "TLS"
            res.append({
                        "name": "香蕉VPN",
                        'type': '3',
                        'FQprotocol1': f1,
                        'FQprotocol2': t,
                        'host': re.search("server: (.*?),", data).group(1),
                        'transfer_protocol': 'TCP',
                        'start_port': re.search("port: (.*?),", data).group(1),
                        'end_port': re.search("port: (.*?),", data).group(1),
                    })
        return res

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [i.strip() for i in datas]


if __name__ == '__main__':
    mxt = ComBananagoNow()
    data = mxt.main("../data/data/com_bananago_now")
    print(data)


