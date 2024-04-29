#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os


class OctohideVpn:
    def main(self, path):
        res = []
        if not os.path.exists(path):
            print("file is not exits.")
            return res

        servers_list = self.get_serverinfo(path)
        print("server list has {0} server.".format(len(servers_list)))
        for server_list in servers_list:
            for server_info in server_list["servers"]:
                host = server_info.get("host")
                port = server_info.get("port")
                proto = server_info.get("proto")
                if host and port:
                    res.append({
                        "name": "OctohideVPN",
                        'type': '0',
                        'FQprotocol1': proto,
                        'FQprotocol2': proto,
                        'host': host,
                        'transfer_protocol': 'UDP',
                        'start_port': port,
                        'end_port': port
                    })
        return res

    def get_serverinfo(self, path):
        print("path: {0}".format(path))
        with open(path, 'r', encoding='utf-8') as fp:
            txt_data = fp.readlines()
            return [json.loads(i) for i in txt_data]


if __name__ == "__main__":
    print("Hello Python")
