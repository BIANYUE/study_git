import requests
from datetime import datetime

# 获取当前时间
current_time = datetime.utcnow()

# 将当前时间转换为目标格式
target_format = current_time.strftime("%a, %d %b %Y %H:%M:%S GMT")
print(target_format)

url = 'http://spacevpn.tech/device/checkVip'

headers = {
    'Cache-Control': 'private',
    'Expires': 'Thu, 01 Jan 1970 00:00:00 GMT',
    'Content-Type': 'text/plain;charset=UTF-8',
    # 'Content-Length': '1689',
    'Date': target_format,
    'Keep-Alive': 'timeout=60',
    'Connection': 'keep-alive'
}

response = requests.get(url, headers=headers)
print(response.text)