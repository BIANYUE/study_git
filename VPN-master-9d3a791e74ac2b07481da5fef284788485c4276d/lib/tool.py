# -*- coding: utf-8 -*-
import configparser
import logging
import os
import re
import time
import traceback
import urllib3
import requests
import yaml

from settings import CONFIG_PATH


cp = configparser.RawConfigParser()
urllib3.disable_warnings()


def wirte_data(data, pathname, typee='a'):
    path = "/".join(pathname.split('/')[:-1])
    # print(path)
    mkdir(path)
    with open(pathname, typee, encoding='utf-8')as fp:
        fp.write(data)


def mkdir(path):
    a = ''
    p = []
    for i in path.split('/'):
        a += i + '/'
        p.append(a + '/')

    for i in p:
        if not os.path.exists(i):
            os.mkdir(i)


def get_config():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as fp:
        return yaml.safe_load(fp)


def get_data(name):
    with open(name, 'r', encoding="utf-8") as fp:
        datas = fp.readlines()
    datas = '\n'.join([i.strip() for i in datas]).split("[*] class enuemration complete\n")[-1].split('\n')
    # print(datas)
    return datas


def catch_exception(cls_func):
    """捕获错误的装饰器"""

    def wrapper(self, *args, **kwargs):
        while True:
            try:
                time.sleep(2)
                result = cls_func(self, *args, **kwargs)
                return result
            except Exception as error:

                return

    return wrapper


def get_classname(file, t=None):
    file = file.replace('.', '/') + '.py'
    with open(file, 'r', encoding='utf-8') as fp:
        data = fp.read()
    # print(data)
    if t:
        classname = re.search('class (.*?):', data).group(1)
    else:
        classname = re.search('class (.*?)\(BaseAppium\)', data).group(1)
    return classname


def get_processname(package):
    return ''.join([i.capitalize() for i in package.split('.')])


def req(url, headers=None, data=None, files=None, method="get", allow_redirects=None):
    proxies = None
    # proxies = {"http": "http://192.168.0.143:8899", "https": "https://192.168.0.143:8899"}
    time.sleep(3)
    while 1:
        try:
            if method == "get":
                response = requests.get(url, headers=headers, verify=False, proxies=proxies,
                                        allow_redirects=allow_redirects, timeout=(30, 30))
            else:
                response = requests.post(url, headers=headers, data=data, verify=False, files=files,
                                         proxies=proxies, timeout=(30, 30))
            return response
        except Exception as e:
            logging.info(traceback.format_exc())
            print(traceback.format_exc())


if __name__ == '__main__':
    package = "me.xhss.tomvpn"
    classname = get_processname(package)
    print(classname)
