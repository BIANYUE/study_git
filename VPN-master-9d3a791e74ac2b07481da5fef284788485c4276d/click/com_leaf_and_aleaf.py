# -*- coding: utf-8 -*-
import re

from lib.tool import req, wirte_data
from settings import DATA_PATH


class ComLeafAndAleaf:
    def __init__(self, app):
        self.headers = {
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; Pixel XL Build/OPM4.171019.021.P1)',
            'Host': 'www.kitslabs.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        datas = self.get_iplist()
        ip_list = self.get_ip(datas)
        # print(ip_list)
        data = re.findall("(.*?host,.*?)\n", datas, re.M)
        for i in data:
            print(i)
            for key, value in ip_list.items():
                if key in i:
                    for ip in value[0].split(","):
                        new_i = i.replace(key, ip.strip())
                        wirte_data(new_i + "\n", self.path_name)

    def get_iplist(self):
        # time.sleep(3)
        url = f"https://www.kitslabs.com/go.and.28.premium.conf"
        response = req(url, headers=self.headers)
        print(response.text)
        return response.text

    def get_ip(self, datas):
        cf_hosts = {}
        for i in range(1, 4):
            cf_host_key = f"cf{i}.host"
            cf_host_value = re.findall(fr"\s*{cf_host_key}\s*=\s*([\d.,\s]+)\s*", datas)
            cf_hosts[cf_host_key] = cf_host_value
        return cf_hosts


if __name__ == '__main__':
    app = {
        'appPackage': 'com.leaf.and.aleaf',
        'package': 'com.leaf.and.aleaf',
        'appActivity': '',
        'click_file': 'com_leaf_and_aleaf',
        'process': 'com_leaf_and_aleaf',
        'data': 'com_leaf_and_aleaf',
        'data_type': 'password',
        'class_name': '',
        'type': 'request',
    }
    cpa = ComLeafAndAleaf(app)
    cpa.main()
