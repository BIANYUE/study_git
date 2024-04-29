import re
import base64


class ComMoguGo:
    def main(self, path):
        datas = self.get_data(path)
        print(datas)
        res = []
        for data in datas:
            d = data.split("@")
            pwd_method = d[0].split(':')
            ip_port = d[1].split(':')

            res.append({
                "name": "蘑菇加速器",
                "host": ip_port[0],
                "start_port": ip_port[1],
                "end_port": ip_port[1],
                "transfer_protocol": "TCP",
                "type": "0",
                "encrypt": pwd_method[0],
                "password": pwd_method[1]
            })
        return res

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [base64.b64decode(i.strip().split("//")[1]).decode() for i in datas]


if __name__ == '__main__':
    mxt = ComMoguGo()
    data = mxt.main("../data/password/com_mogu_go")
    print(data)
