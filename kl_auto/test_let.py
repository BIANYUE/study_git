import time
import multiprocessing
import pyshark
from scapy.all import rdpcap
from selenium import webdriver

class KuailianAutomation:
    def __init__(self):
        self.desired_caps = {}
        self.desired_caps['app'] = r"G:\fast\letsvpn\app-3.3.14\LetsPRO.exe"
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=self.desired_caps
        )

    def wireshark(self):
        for i in range(1):
            tshark_path = "E:\\软件1\\weka\\Wireshark\\tshark.exe"
            current_timestamp = time.time()
            print(int(current_timestamp))
            time.sleep(10)
            capture = pyshark.LiveCapture(output_file="./data/" + "kuailian" + ".pcapng",
                                          interface="以太网", bpf_filter='tcp', tshark_path=tshark_path)
            while True:
                capture.sniff(timeout=30)
            # 每次抓包的超时时间为10秒

    def auto_click(self):
        time.sleep(5)
        self.driver.find_element_by_name("首页").click()
        time.sleep(5)
        elements = self.driver.find_elements_by_name("开启快连")
        for i in range(2):
            time.sleep(5)
            elements[2].click()

    def kuailian_auto(self):
        self.auto_click()
        time.sleep(5)
        countries = ["阿联酋", "香港", "印尼", "印度", "日本", "韩国",
                     "马来西亚", "菲律宾", "新加坡", "泰国", "台湾", "越南",
                     "瑞士", "德国", "西班牙", "法国", "爱尔兰", "意大利",
                     "荷兰", "挪威", "波兰", "俄罗斯", "瑞典", "土耳其", "英国",
                     "尼日利亚", "澳大利亚", "加拿大", "墨西哥", "美国",
                     "阿根廷", "巴西"]
        for country in countries:
            self.driver.find_element_by_name("网络配置").click()
            time.sleep(5)
            self.driver.find_element_by_name(country).click()
            time.sleep(5)
            self.auto_click()
        print("抓包完毕")
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

    def run(self):
        wireshark_process = multiprocessing.Process(target=self.wireshark)
        kuailian_process = multiprocessing.Process(target=self.kuailian_auto)

        wireshark_process.start()
        kuailian_process.start()

if __name__ == '__main__':
    automation = KuailianAutomation()
    automation.run()
