# -*- coding:utf-8 -*-
"""
@Time: 2022/9/27 13:47
@Author: zxq
@File: 练习2：豆瓣.py
"""
import urllib.request
import urllib.parse
# POST的请求
url = 'https://accounts.douban.com/j/mobile/login/basic'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Cookie": 'll="108303"; bid=2uxBzfAbsC8; __gads=ID=525d5988ffda689e-225a3fecbad600e8:T=1664350986:RT=1664350986:S=ALNI_MbmlllxhaZ5eBMMpPPU_Q4UsWKyeg; push_noty_num=0; push_doumail_num=0; __utmv=30149280.26318; apiKey=; __utma=30149280.1938558455.1663727730.1664354747.1665130603.6; __utmc=30149280; __utmz=30149280.1665130603.6.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; last_login_way=account; ap_v=0,6.0; __gpi=UID=000009e9b2767cef:T=1664350986:RT=1665130675:S=ALNI_MYfelmEzjh1rTo9Z3WBq1HXJDHQMw; __utmb=30149280.6.10.1665130603; login_start_time=1665130776722'
}
data = {
    "remember": "true",
    "name": 18039518322,
    "password": 123456
}
info = bytes(urllib.parse.urlencode(data).encode('utf-8'))
request = urllib.request.Request(url, headers=headers, data=info)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

