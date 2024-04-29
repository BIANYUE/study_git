#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import os
import time
import shutil
import sqlite3

from lib.tool import wirte_data
from settings import DATA_PATH
from click.base_appnium import BaseAppium


class Squirrelvpn:
    def __init__(self, app):
        self.ba = BaseAppium(app["deviceName"], app["appPackage"], app["appActivity"], app["platformVersion"],
                             app["host"], app["port"])
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        cmd_file = "data/com_squirrelvpn_cmd.txt"
        server_config = "data/RKStorage"
        server_info = {"servers": []}
        time.sleep(60)

        self.get_serverconfig(cmd_file)
        if os.path.exists(server_config):
            conn = sqlite3.connect(server_config)
            cur = conn.cursor()

            sql_cmd = "SELECT key,value From catalystLocalStorage"
            cur.execute(sql_cmd)
            all_data = cur.fetchall()
            # print(type(all_data))
            # print(all_data)
            key_list = [keyword[0] for keyword in all_data]
            # print(key_list)
            network_index = key_list.index("CurrentNetwork")
            # print("network index: {0}".format(network_index))
            json_data = json.loads(all_data[network_index][1])
            # print(json_data["rawData"].keys())
            for proxy_server in json_data["rawData"]["proxyServerList"]:
                if "ss" in proxy_server:
                    host = proxy_server["ss"]["ip"]
                    port = proxy_server["ss"]["ps_port"]
                    if not host or not port or host == "" or port == "":
                        pass
                    else:
                        server_info["servers"].append({"host": host, "port": port, "proto": "ss"})
                if "trojan" in proxy_server:
                    host = proxy_server["trojan"]["trojan_domain"]
                    port = proxy_server["trojan"]["trojan_port"]
                    if not host or not port or host == "" or port == "":
                        pass
                    else:
                        server_info["servers"].append({"host": host, "port": port, "proto": "trojan"})

            print(server_info)
            if len(server_info["servers"]) > 0:
                dump_data = json.dumps(server_info)
                wirte_data(dump_data + "\n", self.path_name)
                time.sleep(5)
            cur.close()
            conn.close()
            time.sleep(5)

            os.remove(server_config)
            time.sleep(5)
            # self.ba.close()

    def get_serverconfig(self, cmd_file):
        os.system("adb shell < {0}".format(cmd_file))
        time.sleep(2)
        os.system("adb pull /sdcard/RKStorage ./data")
        time.sleep(5)


if __name__ == "__main__":
    print("Hello Python")
    app = {
        'appPackage': 'com.squirrelvpn',
        'package': 'com.squirrelvpn',
        'appActivity': 'com.squirrelvpn.MainActivity',
        'click_file': 'com_squirrelvpn',
        'process': 'com_squirrelvpn',
        'data': 'com_squirrelvpn',
        'data_type': 'com.gopher.mobile.ProxyService',
        'class_name': '',
        'type': 'request',
    }

    squirrelvp = Squirrelvpn(app)
    squirrelvp.main()
