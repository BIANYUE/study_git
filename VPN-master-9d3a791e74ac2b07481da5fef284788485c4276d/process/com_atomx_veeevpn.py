import json
import re

class ComAtomxVeeevpn:
    def main(self, path):
        res = []
        datas = self.get_data(path)
        for data in datas:
            bean = json.loads(data)["bean"]
            res.append({
                        "name": "Veee",
                        'type': '3',
                        'FQprotocol1': "SS",
                        'FQprotocol2': "SS",
                        'host': bean["ip"],
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
    mxt = ComAtomxVeeevpn()
    data = mxt.main("../data/data/com_atomx_veeevpn")
    print(data)


