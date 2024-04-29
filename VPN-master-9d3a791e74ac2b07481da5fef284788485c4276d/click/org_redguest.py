# -*- coding: utf-8 -*-
import time
import gzip
import hashlib
import json
import os
import time
import sqlite3

# org.rocket
from lib.tool import req, wirte_data
from settings import DATA_PATH


# org.redguest
class OrgRedguest:
    def __init__(self, app):
        self.headers = {
            'User-Agent': 'OkHttp/3.0 (Android)--qie-apk_27-0.0.7',
            # 'Host': '202.64.1.64:15253',
            'Host': '42.51.18.42:12472',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
        }
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        self.get_list()
        ip_list = self.get_sql()
        for target in ip_list:
            data = self.get_ip(target[0])
            if "server" in data:
                print(data)
                wirte_data(data + "\n", self.path_name)
        os.remove('temp_db1')

    def get_sql(self):
        conn = sqlite3.connect('temp_db1')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM static_tbl')
        rows = cursor.fetchall()

        # for row in rows:
        #     print(row)
        data = [i for i in rows]
        print(data)
        conn.close()
        return data

    def get_ip(self, target):
        # url = "https://202.64.1.64:15253/client-ad01.php"
        url = "https://42.51.18.42:12472/client-ad01.php"
        p = str(int(int(time.time()*1000) / 1000 / 300)) + "d8217dee9f7d8b3ef8b27407efff43daads"
        data = {
            'app': 'get_static_cfg2',
            'pass': str(hashlib.md5(p.encode()).hexdigest()),
            #'user': 'd8217dee9f7d8b3ef8b27407efff43da',
            'user':'d8217dee9f7d8b3ef8b27407efff43da',
            'target': target,

        }
        print(data)
        self.headers["Content-Type"] = "application/x-www-form-urlencoded"
        response = req(url, headers=self.headers, data=data, method="post")
        print(response.text)
        return response.text

    def get_list(self):
        # url = "https://202.64.1.64:15253/srvs-red.db.gz"
        url = "https://42.51.18.42:12472/srvs-red.db.gz"
        response = req(url, headers=self.headers)
        # print(response.content)
        data = response.content
        new_data = gzip.decompress(data)
        # print(new_data)
        with open("temp_db1", 'wb')as fp:
            fp.write(new_data)






if __name__ == '__main__':
    app = {
        'appPackage': 'org.rocket',
        'package': 'org.rocket',
        'appActivity': '',
        'click_file': 'org_rocket',
        'process': 'org_rocket',
        'data': 'org_rocket',
        'data_type': 'password',
        'class_name': '',
        'type': 'request',
    }
    or_ = OrgRedguest(app)
    or_.main()
