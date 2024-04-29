import re


class ComHidecatMine:
    def main(self, path):
        datas = self.get_data(path)

        return [{
            "name": "Hidecat",
            'type': '3',  # 这个字段必须有，写死成"3"即可
            'FQprotocol1': 'SS',  # FQ协议 （没有为"null"）
            'FQprotocol2': 'SS',  # FQ子协议（没有为"null"）
            'host': re.search("@(.*?):", data).group(1),  # ip/host
            'transfer_protocol': 'TCP',  # 传输协议
            'start_port': re.search(".*:(.*?)#", data).group(1),  # 起始端口 （若只有一个端口号则起始端口和结束端口值相同）
            'end_port': re.search(".*:(.*?)#", data).group(1),  # 结束端口
        } for data in datas]

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as fp:
            datas = fp.readlines()
        return [i.strip() for i in datas]


if __name__ == '__main__':
    mxt = ComHidecatMine()
    data = mxt.main("../data/data/com_hidecat_mine")
    print(data)


