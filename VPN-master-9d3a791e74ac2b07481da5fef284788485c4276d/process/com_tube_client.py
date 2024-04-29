import json
import re

class ComTubeClient:
    def main(self, path):
        res = []
        datas = self.get_data(path)
        for data in datas:
            # print(data)
            res.append({
                        "name": "TubeVPN",
                        'type': '3',
                        'FQprotocol1': 'OTHER',
                        'FQprotocol2': 'TLS',
                        'host': re.search(r"'host': '(.*?)',", data).group(1).split(",")[0],
                        'transfer_protocol': 'TCP',
                        'start_port': re.search("'remotePort': (.*?),", data).group(1),
                        'end_port': re.search("'remotePort': (.*?),", data).group(1),
                    })
        return res

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [i.strip() for i in datas]


if __name__ == '__main__':
    mxt = ComTubeClient()
    data = mxt.main("../data/data/com_tube_client")
    print(data)


