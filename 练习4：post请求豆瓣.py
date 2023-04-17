# -*- coding:utf-8 -*-
"""
@Time: 2022/9/28 15:45
@Author: zxq
@File: 练习4：post请求豆瓣.py
"""
import requests
import json
# 登陆url
url = 'https://accounts.douban.com/j/mobile/login/basic'
# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Cookie": 'll="108303"; bid=2uxBzfAbsC8; __utma=30149280.1938558455.1663727730.1664261848.1664350983.4; __utmc=30149280; __utmz=30149280.1664350983.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; __gads=ID=525d5988ffda689e-225a3fecbad600e8:T=1664350986:RT=1664350986:S=ALNI_MbmlllxhaZ5eBMMpPPU_Q4UsWKyeg; __gpi=UID=000009e9b2767cef:T=1664350986:RT=1664350986:S=ALNI_MYfelmEzjh1rTo9Z3WBq1HXJDHQMw; apiKey=; user_data={%22area_code%22:%22+86%22%2C%22number%22:%2218039518322%22%2C%22code%22:%224677%22}; vtoken=phone_register%205a31fb039b354a67867e92fc3014211e; last_login_way=phone; push_noty_num=0; push_doumail_num=0; __utmv=30149280.26318; __utmt=1; __utmb=30149280.20.10.1664350983; login_start_time=1664351648477'
}
# 参数
data = {
    "remember": "true",
    "name": "18039518322",
    "password": "zxq123456"
}
# 创建session对象；保持会话
session = requests.session()
resp = session.post(url, data=data, headers=headers)
resp.encoding = 'utf-8'
print(resp.text)   # 成功

# 个人信息GET请求
url1 = 'https://www.douban.com/people/263183887/'
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Referer": "https://www.douban.com/"
}
res1 = session.get(url1, headers=headers1)
print(res1.text)
