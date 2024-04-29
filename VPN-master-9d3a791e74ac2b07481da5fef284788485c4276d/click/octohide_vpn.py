#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import json
import time
import math

from lib.tool import req, wirte_data
from settings import DATA_PATH


class OctohideVpn:
    # construct header
    def __init__(self, app):
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Content-Length': str(len(json.dumps(data, separators=(',', ":")))),
            'Host': 'mobile.octohide.com',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'Android: 8.1.0; App name: octohide.vpn; Device: Pixel XL; App version: v2.126; Version code: 126;',
            'Connection': 'Keep-Alive'
        }

        self.path_name = '/'.join([DATA_PATH, app["data_type"], app["data"]])

    def main(self):
        rep_txt = self.get_serverResponse()
        server_info = self.get_serverinfo(rep_txt)
        dump_data = json.dumps(server_info)
        wirte_data(dump_data + "\n", self.path_name)

    def get_serverinfo(self, rep_txt):
        connet_key = "connect"
        host_key = "public_ip"
        port_key = "port"
        proto_key = "type"
        server_info = {"servers": []}

        info_dic = json.loads(rep_txt)
        if connet_key in info_dic:
            if host_key in info_dic[connet_key]:
                host = info_dic[connet_key][host_key]
            if port_key in info_dic[connet_key]:
                port = info_dic[connet_key][port_key]
            if proto_key in info_dic[connet_key]:
                proto = info_dic[connet_key][proto_key]

        server_info["servers"].append({"host": host, "port": port, "proto": proto})
        print("server info: {0}".format(server_info))

        return server_info

    def get_serverResponse(self):
        url = f"https://mobile.octohide.com/api/v2/"
        data = {
            'action[1]': 'connect',
            'action[0]': 'publicip',
            'connection_type': 'wifi',
            'os': 'Android',
            'device_model': 'Pixel XL',
            'os_version': '8.1.0',
            'platformid': '74739b',
            'locale': 'zh-CN',
            'mtu': '1280',
            'service': '1',
            'requestid': '627a63f17f4c3b45',
            'configid': '08278277',
            'pkey': 'PdXvqu81dB7IUZdTABX1WRpkm0ca6ZXWA7hG0loDXDg=',
            'id': '38c0ec9ed224ef59',
            'install_source': '',
            'region': '0',
            'client_version': 'v2.126',
            'timestamp': str(math.ceil(time.time()))
        }

        response = req(url, headers=self.headers, data=data, method="post")

        print("response txt: {0}".format(response.text))

        return response.text


if __name__ == '__main__':
    print("Hello Python")
    app = {
        'data': 'octohide_vpn',
        'data_type': 'data'
    }
    octohide_app = OctohideVpn(app)
    octohide_app.main()
