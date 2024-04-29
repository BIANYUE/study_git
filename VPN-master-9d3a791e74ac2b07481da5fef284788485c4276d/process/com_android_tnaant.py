import json
import re


class ComAndroidTnaant:
    def main(self, path):
        res = []
        datas = self.get_data(path)
        print(datas)
        for d in datas:
            res.extend([{
                "name": "蚂蚁加速器",
                "host": data["ip"],
                "start_port": data["port"],
                "end_port": data["port"],
                "transfer_protocol": "TCP",
                "type": "0",
                "encrypt": data["method"],
                "password": data["passwd"]
            } for data in d])
        return res

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [json.loads(i.strip()) for i in datas]


if __name__ == '__main__':
    mxt = ComAndroidTnaant()
    data = mxt.main("../data/password/com_android_tnaant")
    print(data)
