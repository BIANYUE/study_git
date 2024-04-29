import json
import re

class ComAttoricVpnHero:
    def main(self, path):
        res = []
        datas = self.get_data(path)
        for data in datas:
            beans = json.loads(data)
            for bean in beans:
                res.append({
                            "name": "Hero VPN",
                            'type': '3',
                            'FQprotocol1': "SS",
                            'FQprotocol2': "SS",
                            'host': bean["ipAddr"],
                            'transfer_protocol': 'TCP',
                            'start_port': bean["b01"],
                            'end_port': bean["b01"],
                        })
        return res

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [i.strip() for i in datas]


if __name__ == '__main__':
    mxt = ComAttoricVpnHero()
    data = mxt.main("../data/data/com_attoric_vpn_hero")
    print(data)


