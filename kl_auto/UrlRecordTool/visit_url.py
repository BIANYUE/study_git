#!usr/bin/python

from selenium import webdriver
import time
from setting import LOOP_INTERVAL_TIME, TARGET_URL_PATH,PAGE_LOAD_TIME_OUT,FILTER_URL_PATH,TSHARK_EXE,IFACE,PCAP_SIZE\
    ,STORAGE_LOCATION
import os
import glob
import codecs
from threading import Thread
from shutil import move
N=0
def read_url(path):
    with codecs.open(path,'r',encoding='utf-8') as f:
        line = f.readlines()
    return [i.strip('\n')for i in line]

def grab_pcap():
    # print("开始抓包")
    os.system("{0}tshark.exe -i {1} -b filesize:{2} -w {3}url.pcapng".format(TSHARK_EXE,
                                                                                 IFACE,
                                                                                 PCAP_SIZE,
                                                                                 STORAGE_LOCATION,
                                                                                 ))

def main():
    if not os.path.exists(TARGET_URL_PATH):
        raise FileExistsError("URL文件不存在")
    if not isinstance(LOOP_INTERVAL_TIME, int):
        raise TypeError("输入的loop interval time 类型不对，必须为数字")
    if not isinstance(PAGE_LOAD_TIME_OUT, int):
        raise TypeError("输入的page time out 类型不对，必须为数字")
    if not os.path.exists(STORAGE_LOCATION):
        os.makedirs(STORAGE_LOCATION)
    url_filter_list = read_url(FILTER_URL_PATH)
    n=0
    if not os.path.exists(os.path.dirname(os.path.abspath("__file__")) + '\\visted_floder'):
        os.mkdir(os.path.dirname(os.path.abspath("__file__")) + '\\visted_floder')
    while True:
        url_files_list =[i for i in  glob.glob('*.txt') if i not in ['target_url.txt','filter.txt']]

        if len(url_files_list) == 0 :
            time.sleep(LOOP_INTERVAL_TIME)
            print('没有url文件，等待一会')
            continue
        for line in url_files_list:
            print(line)
            url_list = read_url(line)
            browser = webdriver.Chrome() #创建chrome驱动
            browser.maximize_window() #窗口最大化
            browser.set_page_load_timeout(PAGE_LOAD_TIME_OUT)  # 设置页面加载超时
            browser.set_script_timeout(PAGE_LOAD_TIME_OUT)
            for url in url_list:
                #添加过滤某些URL的语句，url从TXT文件中获取
                if url in url_filter_list:
                    continue
                if len(url) < 0:
                    continue
                try:
                    t = Thread(target=grab_pcap)
                    t.start()
                    time.sleep(5)
                    print(url)
                    browser.get(url)
                except Exception as e :  # 捕获timeout异常
                    print(e)
                    os.system("taskkill /im tshark.exe /f")
                    continue

                n += 1
                time.sleep(LOOP_INTERVAL_TIME)

                if len(browser.window_handles) > 1:
                    browser.switch_to.window(browser.window_handles[-1])
                    browser.close()
                    browser.switch_to.window(browser.window_handles[0])
                print("停止抓包")
                os.system("taskkill /im tshark.exe /f")

            browser.quit() #关闭浏览器

            move(os.path.dirname(os.path.abspath("__file__")) + '\\' + line, os.path.dirname(os.path.abspath("__file__")) + '\\visted_floder')
            # except Exception as e:
            #     continue


if __name__ == "__main__":
    main()
