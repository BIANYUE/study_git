import re


class ComKeynoteFreeAndroid:
    def main(self, path):
        datas = self.get_data(path)
        return [{
            "name": "keynote",
            'type': '3',
            'FQprotocol1': 'SS',
            'FQprotocol2': 'SS',
            'host': data.split(':')[0],
            'transfer_protocol': 'TCP',  # 传输协议
            'start_port': data.split(':')[1],
            'end_port': data.split(':')[1],
        } for data in datas]

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [re.search("@(.*?)#", i.strip()).group(1) for i in datas if "Q0hBQ0hBMjAtSUVURi1QT0xZMTMwNTpTTXNqNHQkdDM3MjY1bnpXeHE1" in i]


if __name__ == '__main__':
    mxt = ComKeynoteFreeAndroid()
    data = mxt.main("../data/data/com_keynote_free_android")
    print(data)


