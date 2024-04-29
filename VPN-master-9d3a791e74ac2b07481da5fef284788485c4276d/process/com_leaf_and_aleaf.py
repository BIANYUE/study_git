import re
import base64


class ComLeafAndAleaf:
    def main(self, path):
        datas = self.get_data(path)
        # print(datas)
        res = []
        for data in datas:
            d = data.split(',')
            if d[0] is None:
                continue
            # print(d)
            # res.append({
            #     "name": "Leaf VPN",
            #     "host": d[1].strip(),
            #     "start_port": d[2].strip(),
            #     "end_port": d[2].strip(),
            #     "transfer_protocol": "TLS",
            #     "type": "0",
            #     "encrypt": d[3].split('=')[1],
            #     "password": d[4].split('=')[1]
            # })
            res.append({
                "name": "Leaf VPN",
                "type": "3",
                'FQprotocol1': "TROJAN",
                'FQprotocol2': "TLS",
                "host": d[1].strip(),
                "transfer_protocol": "TCP",
                "start_port": d[2].strip(),
                "end_port": d[2].strip()
            })
        # print(res)
        return res

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
            # print(datas)
        return [i.strip() for i in datas]


if __name__ == '__main__':
    mxt = ComLeafAndAleaf()
    data = mxt.main("../data/password/com_leaf_and_aleaf")
    print(data)
