import json
import re


class ComZgXhnGoogle:
    def main(self, path):
        res = []
        datas = self.get_data(path)
        print(datas)
        for d in datas:
            res.extend([{
                "name": "小黑牛",
                "host": data["server_ip"],
                "start_port": data["server_port"],
                "end_port": data["server_port"],
                "transfer_protocol": "TCP",
                "type": "0",
                "encrypt": data["encryption"],
                "password": data["server_pwd"]
            } for data in d])
        return res

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [json.loads(i.strip()) for i in datas]


if __name__ == '__main__':
    mxt = ComZgXhnGoogle()
    data = mxt.main("../data/password/com_zg_xhn_google")
    print(data)
