# -*- coding:utf-8 -*-
"""
@Time: 2022/9/28 16:49
@Author: zxq
@File: 练习5：百度贴吧.py
"""
import requests
url = 'https://tieba.baidu.com/'
params = {
    'ie': 'utf-8',
    'kw': '正则表达式',
    'fr': 'search'
}
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
sessions = requests.session()
resp = sessions.get(url, params=params, headers=headers)
print(resp.text)