import os
import time
import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from setting import TARGET_URL_PATH, TIME_OUT, LEVEL_NUMBER, DEPTH, URL_LINES,URL_MAX
from bs4 import BeautifulSoup
import codecs
import shutil
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

import traceback


def read_url_from_txt(path):
    with open(path, 'r') as f:
        url_list = f.readlines()
    return url_list


class Url:
    def __init__(self):
        self.record_url_file_number = 0
        self.url_lines = URL_LINES
        self.depth = DEPTH
        self.level_number = LEVEL_NUMBER
        self.records_url_list = list()



    def get_out_in_url(self,url):
        if url is None:
            return [],[]
        in_list = []
        out_list = []
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'}
        try:
            page = requests.get(url, verify=False, timeout=TIME_OUT, headers=headers).text

        except requests.RequestException as e:
            print("get " + url + " timeout")
            return [], []

        try:
            self.save_file()
            soup = BeautifulSoup(page, 'lxml')
            zzr = soup.find_all('a')
            for item in zzr:
                try:
                    line = item.get("href")
                    if line is None:continue
                    if 'down' in line or re.match(str('http[s]?://'), str(line), flags=0) is None:
                        continue
                    if re.match(str('http[s]?://www'),str(line), flags=0):
                        out_list.append(line)
                    else:
                        #"?" in line or line.endswith('/') or
                        if  line.endswith('shtml') or line.endswith(
                                'html') or line.endswith('php') or line.endswith('jsp') \
                                or line.endswith('asp') or line.endswith('aspx'):
                            in_list.append(line)
                    if len(in_list) > self.level_number:
                        in_list = in_list[:self.level_number - 1]
                except Exception as e:
                    print(e)
                    continue
        except Exception as e:
            print(traceback.print_exc())

        return out_list, in_list

    def save_file(self):
        try:
            if self.records_url_list.__len__() > self.url_lines:
                txt_file = "url_"+str(self.record_url_file_number)+'.txt'
                if os.path.exists("url_"+str(self.record_url_file_number)+'.txt'):
                    txt_file = "url_"+str(self.record_url_file_number)+'s'+'.txt'
                with codecs.open(txt_file, 'w+',encoding='utf-8') as f:
                    f.writelines(self.records_url_list)
                    f.flush()
                self.records_url_list.clear()
                self.record_url_file_number += 1
        except Exception as e:
            print(e)




    def main(self):

        if not os.path.exists(TARGET_URL_PATH):
            raise FileNotFoundError("目标文件不存在")

        url_list = read_url_from_txt(TARGET_URL_PATH)
        for url in url_list:
            # self.bak_name = url.split('.')[1]
            # if not os.path.exists(self.bak_name):
            #     os.mkdir(self.bak_name)
            # else:
            #     shutil.rmtree(self.bak_name)
            #     os.mkdir(self.bak_name)
            out_url, in_url = self.get_out_in_url(url)
            print(in_url)
            try:
                # 先对内链进行遍历
                while self.depth > 1:
                    url_list_tmp = set([])
                    for url in in_url:
                        print(url)
                        try:
                            self.records_url_list.append(url+'\n')
                            a = self.get_out_in_url(url)[1]
                            url_list_tmp.update(a)
                            self.save_file()
                        except:
                            print(e)
                            continue
                    in_url = url_list_tmp
                    self.depth = self.depth - 1
                # 对外链进行遍历
                while out_url:
                    url_list_tmp = set([])
                    for url in out_url:
                        print(url)
                        try:
                            self.records_url_list.append(url+'\n')
                            a = self.get_out_in_url(url)[0]
                            url_list_tmp.update(a)
                            self.save_file()
                        except Exception as e:
                            print(e)
                            continue
                    if url_list_tmp.__len__() > URL_MAX:
                        out_url = list(url_list_tmp)[0:URL_MAX]
                    else:
                        out_url = list(url_list_tmp)
                    print(len(out_url))

            except Exception as e:
                print(e)
                continue



if __name__ == "__main__":
    Url().main()
