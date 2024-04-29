# -*- coding: utf-8 -*-
import os

import frida
import sys

from lib.tool import wirte_data
from settings import FRIDA_JSCODE_PATH, DATA_PATH


class FirdaPython:
    def __init__(self, path_name, data_type):
        self.path_name = '/'.join([DATA_PATH, data_type, path_name])
        # if os.path.exists(self.path_name):
        #     os.remove(self.path_name)

    def on_message(self, message, data):  # 该函数可在frida中使用send(a); 输出python类型内容
        if message['type'] == 'send':
            # print("[*] {0}".format(message['payload']))
            self.save_data(message['payload'])
        else:
            print("message:  ", message)

    def save_data(self, data):
        wirte_data(data + "\n", self.path_name)

    def replace_jscode(self, class_name):
        with open(FRIDA_JSCODE_PATH, 'r', encoding='utf-8') as fp:
            jscode = fp.read()

        return jscode.replace('hookClass("")', f'hookClass("{class_name}")')

    def hook_class(self, packge, class_name):
        rdev = frida.get_remote_device()
        # process = rdev.enumerate_processes()
        session = rdev.attach(packge)
        script = session.create_script(self.replace_jscode(class_name))
        script.on('message', self.on_message)
        script.load()
        sys.stdin.read()


if __name__ == '__main__':
    packge = "me.xhss.tomvpn"
    class_name = "me.xhss.tomvpn.TrojanConfig"
    fp = FirdaPython()
    fp.hook_class(packge, class_name)
