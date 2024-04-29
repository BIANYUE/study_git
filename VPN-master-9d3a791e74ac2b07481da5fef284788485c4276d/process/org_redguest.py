import json
import re

# "name": "极客加速器",
class OrgRedguest:
    def main(self, path):
        datas = self.get_data(path)
        res = []
        for data in datas:
            data = data["cfgs"]
            res.append({
                "name": "极客加速器",
                "host": self.get_host(int(data["server"])),
                "start_port": data["ss_port"],
                "end_port": data["ss_port"],
                "transfer_protocol": "TCP",
                "type": "0",
                "encrypt": data["ssmethod"],
                "password": data["ss_key"]
            })
        return res

    def get_host(self, server):
        return ".".join(
            [str((server >> 24) & 255), str((server >> 16) & 255), str((server >> 8) & 255), str(server & 255)])

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [json.loads(i.strip()) for i in datas]


if __name__ == '__main__':
    mxt = OrgRedguest()
    data = mxt.main("../data/password/org_redguest")
    print(data)


