import json
import re
import base64

# i = "vmess://eyJ2IjoiMiIsInBzIjoianAiLCJhZGQiOiIzOC40Ny4xMjcuNCIsInBvcnQiOiI1MDE0NiIsImlkIjoiN2NmMzU3YzQtZWEwMy00MjZkLWFkYzQtNDI0ZjU4YjM5Y"
# data = i.strip().split("//")[1]
# print(data[:-1])
# print(base64.b64decode(data[:-1]))

class DataProcessor:
    def __init__(self):
        self.unique_entries = set()

    def process_data(self, input_file, output_file):
        with open(input_file) as f:
            datas = f.readlines()
            for data in datas:
                if 'vmess://' in data:
                    pattern = r'vmess://([^"]*)'
                    url = re.search(pattern, data).group(1)
                    try:
                        decoded_url = base64.b64decode(url.strip()[:-1]).decode('utf-8')
                        print(decoded_url)
                    except:
                        decoded_url = base64.b64decode(url + '==').decode('utf-8')
                        print(decoded_url)

                    pattern = r'"add":"(.*?)","port":"(.*?)"'
                    match = re.search(pattern, decoded_url)
                    if match:
                        entry = (match.group(1), match.group(2))
                        if entry not in self.unique_entries:
                            self.unique_entries.add(entry)
                            print(match.group(1), match.group(2))
                            with open(output_file, 'a', encoding='utf-8') as f_out:
                                f_out.write("星云加速器" + '\t' + '3' + '\t' + 'VMESS' + '\t' + 'TLSWS' + '\t' +
                                            match.group(1) + '\t' + "TCP" + '\t' + match.group(2) + '\t' + match.group(2) + '\n')

if __name__ == "__main__":
    processor = DataProcessor()
    processor.process_data('./data/111.txt', '星云加速器.txt')

