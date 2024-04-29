import time
from appium import webdriver
import pyshark
import time
import random
import multiprocessing
from scapy.all import *
stop_event = None

# desired_caps = {}
# desired_caps['app'] = r"F:\kuailian\letsvpn\app-3.3.14\LetsPRO.exe"
# driver = webdriver.Remote(
# command_executor='http://127.0.0.1:4723',
# desired_capabilities=desired_caps)
#
# def wireshark():
#     for i in range(1):
#         # tshark_path = "E:\\软件1\\weka\\Wireshark\\tshark.exe"
#         tshark_path = "C:\\Program Files\\Wireshark\\tshark.exe"
#         time.sleep(10)
#         capture = pyshark.LiveCapture(output_file="./data/" + "kuailian" + ".pcapng",
#                                       interface="以太网 2", bpf_filter='tcp', tshark_path=tshark_path)
#         while True:
#             capture.sniff(timeout=600000)
#         # 每次抓包的超时时间为10秒
#
# def auto_click():
#     time.sleep(5)
#     driver.find_element_by_name("首页").click()
#     time.sleep(5)
#     element = driver.find_elements_by_name("关闭")
#     if element:
#         element[1].click()
#         time.sleep(5)
#     elements = driver.find_elements_by_name("开启快连")
#     for i in range(100):
#         print(i)
#         time.sleep(6)
#         elements[2].click()
#         element = driver.find_elements_by_name("关闭")
#         if element:
#             element[1].click()
#             time.sleep(5)
# def auto_click1():
#     time.sleep(5)
#     driver.find_element_by_name("首页").click()
#     time.sleep(8)
#     element = driver.find_elements_by_name("关闭")
#     if element:
#         element[1].click()
#         time.sleep(5)
#     elements = driver.find_elements_by_name("开启快连")
#     for i in range(20):
#         print(i)
#         time.sleep(6)
#         elements[2].click()
#         element = driver.find_elements_by_name("关闭")
#         if element:
#             element[1].click()
#             time.sleep(5)
#
def kuailian_auto():
#     # auto_click()
#     time.sleep(5)
#     countries = [ "阿联酋", "香港", "印尼", "印度", "日本", "韩国",
#              "马来西亚", "菲律宾", "新加坡", "泰国", "台湾", "越南",
#                  "瑞士", "德国", "西班牙", "法国", "爱尔兰", "意大利",
#                  "荷兰", "挪威", "波兰", "俄罗斯", "瑞典", "土耳其", "英国",
#                  "尼日利亚", "澳大利亚", "加拿大", "墨西哥", "美国",
#                  "阿根廷", "巴西"]
#     for country in countries:
#         print(country)
#         driver.find_element_by_name("网络配置").click()
#         time.sleep(5)
#         element = driver.find_elements_by_name("关闭")
#         if element:
#             element[1].click()
#             time.sleep(5)
#         driver.find_element_by_name(country).click()
#         time.sleep(5)
#         element = driver.find_elements_by_name("关闭")
#         if element:
#             element[1].click()
#             time.sleep(5)
#         auto_click1()
#     print("抓包完毕")
    print("开始解析数据包")
    ip_list = []
    pkts = rdpcap('./data/kuailian.pcapng')
    for pkt in pkts:
        # print(pkt.summary())
        with open("kuailian.txt", "a", encoding="utf-8") as f:
            if "TCP 192.168.0.237" in pkt.summary():
                if "1.1.1.1" in pkt.summary():
                    continue
                print(pkt.summary().split()[7].split(":")[0])
                if pkt.summary().split()[7].split(":")[0] in ip_list:
                    continue
                else:
                    ip_list.append(pkt.summary().split()[7].split(":")[0])
                f.write(
                    "快连" + "\t" + "3" + "\t" + "TROJAN" + "\t" + "TLS" + "\t" + pkt.summary().split()[7].split(":")[
                        0] + "\t" +
                    "TCP" + "\t" + "443" + "\t" + "443" + "\n")
        f.close()
    print("end")


if __name__ == '__main__':
    # wireshark_process = multiprocessing.Process(target=wireshark)
    # kuailian_process = multiprocessing.Process(target=kuailian_auto)
    #
    # wireshark_process.start()
    # kuailian_process.start()
    kuailian_auto()




