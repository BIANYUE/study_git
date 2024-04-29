import os

from lib.db.RedisServer import RedisServer
from lib.python_frida import FirdaPython
from settings import REDIS_VPN_PID
import argparse

# 初始化参数构造器
parser = argparse.ArgumentParser()

# 在参数构造器中添加两个命令行参数
parser.add_argument('--config', type=str)

# 获取所有的命令行参数
args = parser.parse_args()


class FridaHook:
    def __init__(self):
        self.s = RedisServer()

    def main(self):
        app = args.config
        self.hook(eval(app))

    def hook(self, app):
        pid = os.getpid()
        # print(pid)
        self.s.rpush(REDIS_VPN_PID, pid)
        packge = app["package"]
        class_name = app["class_name"]
        fp = FirdaPython(app["data"], app["data_type"])
        fp.hook_class(packge, class_name)


if __name__ == '__main__':
    fh = FridaHook()
    fh.main()
