# -*- coding: utf-8 -*-
import json
import logging
import os
import time
import importlib
import traceback
from lib import log
from importlib import reload

# from lib.db.MySQLServer import MySQLServer
from lib.db.RedisServer import RedisServer
from lib.tool import get_config, get_classname, get_processname, mkdir
from settings import REDIS_VPN_PID

from multiprocessing import Process


class VPN:
    def __init__(self):
        self.config = get_config()
        self.s = RedisServer()
        # self.m = MySQLServer()

    def main(self):
        self.click_hook()
        self.process_data()

    def process_data(self):
        t = time.time()
        time_path = time.strftime("%Y_%m_%d", time.localtime(t))
        for app in self.config["app"]:
            # print(app)
            try:
                vpn_data = [json.loads(i) for i in list(set([json.dumps(i) for i in self.start_process(app)]))]
                if len(vpn_data) > 0:
                    save_path = "/".join([self.config["vpn_save_path"], time_path, app["data_type"]])
                    tt = self.vpn_data_save(vpn_data, save_path, t, app["data_type"])
                    self.log_addip(vpn_data, app["process"], tt)
            except Exception as e:
                print(traceback.format_exc())
                logging.info(f"VPN數據清洗出错，配置信息：{app}；错误信息：{traceback.format_exc()}")

    def vpn_data_save(self, datas, path, t, data_type):
        tt = time.strftime("%Y%m%d%H%M", time.localtime(t))
        dd = ['name', 'type', 'FQprotocol1', 'FQprotocol2', 'host', 'transfer_protocol', 'start_port', 'end_port']

        if data_type == "password":
            d = ["name", "host", "transfer_protocol", "start_port", "end_port", "encrypt", "type", "password"]
            self.save(path, datas, tt, d, data_type)
            path = path.replace("password", "data")
            self.save(path, datas, tt, dd, "data")
        else:
            self.save(path, datas, tt, dd, data_type)
        return tt

    def log_addip(self, vpn_data, process_name, tt):
        first_ip_len, now_ip_len, add_len = self.add_iplen(vpn_data, process_name)
        if first_ip_len == 0:
            growth_rate = str(add_len)
        else:
            growth_rate = "%.4f" % (add_len / first_ip_len)
        d = {
            "time": tt,
            "app": process_name,
            "last": first_ip_len,
            "now": now_ip_len,
            "growth": add_len,
            "growth_rate": growth_rate,
        }
        # sql = 'insert into growth(time, app, last, now, growth, growth_rate) values("%s", "%s", "%s", "%s", "%s", "%s")'
        # data = (tt, process_name, first_ip_len, now_ip_len, add_len, "%.4f" % (add_len / first_ip_len))
        # self.m.update(sql, data)
        with open("growth", 'a', encoding='utf-8') as fp:
            fp.write(json.dumps(d, ensure_ascii=False) + '\n')

    def add_iplen(self, vpn_data, process_name):
        key = ':'.join(["vpn", process_name])
        first_ip_len = self.s.scard(key)
        for vpn in vpn_data:
            if vpn["start_port"] == vpn["end_port"]:
                ip_port = ':'.join([vpn["host"], str(vpn["start_port"])])
                self.s.sadd(key, ip_port)
            else:
                for port in range(int(vpn["start_port"]), int(vpn["end_port"]) + 1):
                    ip_port = ':'.join([vpn["host"], str(port)])
                    self.s.sadd(key, ip_port)
        now_ip_len = self.s.scard(key)
        return first_ip_len, now_ip_len, now_ip_len - first_ip_len

    def save(self, path, datas, tt, d, data_type):
        mkdir(path)
        path_name = '/'.join([path, tt])
        data_list = []
        for data in datas:
            if data_type == "data":
                data["type"] = "3"
            data_list.append('\t'.join([str(data.get(i, "SS")) for i in d]))
        data_list = list(set(data_list))
        with open(path_name, 'a', encoding='utf-8') as fp:
            fp.write('\n'.join(data_list) + '\n')

    def start_process(self, app):
        module_name = f'process.{app["process"]}'
        metaclass = importlib.import_module(module_name)
        s = f'metaclass.{get_processname(app["appPackage"])}().main("./data/{app["data_type"]}/{app["data"]}")'
        c = eval(s)
        return c

    def click_hook(self):
        for app in self.config["app"]:
            reload(log)
            try:
                if app["type"] == "request":
                    self.request(app)
                else:
                    self.click_app(app)
                    # break
            except Exception as e:
                logging.info(f"VPN數據提取出错，配置信息：{app}；错误信息：{traceback.format_exc()}")

    def request(self, app):
        module_name = f'click.{app["click_file"]}'
        metaclass = importlib.import_module(module_name)
        app.update({
            "deviceName": self.config["deviceName"],
            "platformVersion": self.config["platformVersion"],
            "host": self.config["host"],
            "port": self.config["port"]
        })
        s = f'metaclass.{get_classname(module_name, True)}({app}).main()'
        eval(s)

    def click_app(self, app):
        self.kill_hook()
        self.s.delete(REDIS_VPN_PID)
        c = self.start_app(app)
        time.sleep(10)
        self.start_hook(app)
        self.click(c)

    def start_app(self, app):
        module_name = f'click.{app["click_file"]}'
        metaclass = importlib.import_module(module_name)
        s = f'metaclass.{get_classname(module_name)}(self.config["deviceName"], app["appPackage"], app["appActivity"], self.config["platformVersion"], self.config["host"], self.config["port"])'
        c = eval(s)  # 调用下面的方法
        return c

    def start_hook(self, app):
        proc = Process(target=hook, args=(app,))
        proc.start()

    def click(self, c):
        time.sleep(5)
        c.main()
        self.kill_hook()

    def kill_hook(self):
        pid = self.s.lpop(REDIS_VPN_PID)
        process = 'TASKKILL /f /pid %s' % pid
        os.system(process)


def hook(app):
    s = f'python frida_main.py --config "{str(app)}"'
    # print(s)
    os.system(s)


if __name__ == '__main__':
    while True:
    # for i in range(1,100):
    #     print(i)
        vpn = VPN()
        vpn.main()
    # vpn.process_data()
