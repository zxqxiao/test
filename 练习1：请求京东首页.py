# -*- coding:utf-8 -*-
"""
@Time: 2022/9/26 19:33
@Author: zxq
@File: 练习1：请求京东首页.py
"""
import urllib.request
requests = urllib.request.Request("http://jd.com")
res = urllib.request.urlopen(requests)
html = res.read().decode("utf-8")
print(html)
