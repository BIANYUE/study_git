import re


class ComHelalikBluespeedVpn:
    def main(self, path):
        datas = self.get_data(path)
        return [{
            "name": "BlueSpeed",
            'type': '3',
            'FQprotocol1': 'VMESS',
            'FQprotocol2': 'TCP',
            'host': data.split(':')[0],
            'transfer_protocol': 'TCP',  # 传输协议
            'start_port': data.split(':')[1],
            'end_port': data.split(':')[1],
        } for data in datas]

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [re.search("@(.*?)\?", i.strip()).group(1) for i in datas if "vless" in i]


if __name__ == '__main__':
    mxt = ComHelalikBluespeedVpn()
    data = mxt.main("../data/data/com_helalik_bluespeed_vpn")
    print(data)


