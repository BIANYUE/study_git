#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import os
import time
import shutil

from lib.tool import wirte_data
from settings import DATA_PATH
from click.base_appnium import BaseAppium


class StrongteamBeevpn:
    def __init__(self, app):
        self.ba = BaseAppium(app["deviceName"], app["appPackage"], app["appActivity"], app["platformVersion"],
                             app["host"], app["port"])
        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        cmd_file = "data/co_strongteam_beevpn_cmd.txt"
        server_dir = "data/files"
        server_info = {"servers": []}
        time.sleep(20)
        self.get_serverconfig(cmd_file)
        config_files = self.find_config(server_dir)
        print("config_files count: {0}".format(len(config_files)))
        for config_file in config_files:
            with open(config_file) as file_handle:
                txt_lines = file_handle.readlines()
                for txt_line in txt_lines:
                    if "remote " in txt_line.lower():
                        str_list = txt_line.split(" ")
                        host = str_list[1]
                        port = str_list[2]
                        server_info["servers"].append({"host": host, "port": port})

        print(server_info)
        dump_data = json.dumps(server_info)
        wirte_data(dump_data + "\n", self.path_name)
        time.sleep(5)




        shutil.rmtree(server_dir)
        time.sleep(5)
        self.ba.close()

    def find_config(self, server_dir):
        config_files = []
        for root, dirs, files in os.walk(server_dir):
            for config_file in files:
                if config_file.endswith(".ovpn") and config_file.startswith("SERVER-"):
                    config_file_path = os.path.join(root, config_file)
                    config_files.append(config_file_path)
        return config_files

    def get_serverconfig(self, cmd_file):
        os.system("adb shell < {0}".format(cmd_file))
        time.sleep(2)
        os.system("adb pull /sdcard/files ./data")
        time.sleep(5)


if __name__ == "__main__":
    print("Hello Python")
    app = {
        'appPackage': 'co.strongteam.beevpn',
        'package': 'co.strongteam.beevpn',
        'appActivity': 'sandok.javacodez.vpn.activities.SplashActivity',
        'click_file': 'co_strongteam_beevpn',
        'process': 'co_strongteam_beevpn',
        'data': 'co_strongteam_beevpn',
        'data_type': 'data',
        'class_name': '',
        'type': 'request',
    }

    beevp = StrongteamBeevpn(app)
    beevp.main()
