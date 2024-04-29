#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os


class ComSquirrelvpn:
    def main(self, path):
        res = []
        if not os.path.exists(path):
            print("process: not found data file.")
            return []

        servers_list = self.get_data(path)
        print(servers_list)
        for server_list in servers_list:
            for server_info in server_list["servers"]:
                host = server_info.get("host")
                port = server_info.get("port")
                proto = server_info.get("proto")

                if host and port and proto:
                    res.append({
                        "name": "Squirrelvpn",
                        'type': '0',
                        'FQprotocol1': proto,
                        'FQprotocol2': proto,
                        'host': host,
                        'transfer_protocol': 'TCP',
                        'start_port': port,
                        'end_port': port
                    })
        print(res)
        return res

    def get_data(self, path):
        print("path: {0}".format(path))
        if not os.path.exists(path):
            print("file is not exits.")
            return None
        with open(path, 'r', encoding='utf-8') as fp:
            txt_data = fp.readlines()

        # json_data = json.load(fp)

        return [json.loads(i) for i in txt_data]


if __name__ == '__main__':
    print("Hello Python!")
    serverinfo_path = "../data/data/com_squirrelvpn"
    squirrelvp = ComSquirrelvpn()
    squirrelvp.main(serverinfo_path)
