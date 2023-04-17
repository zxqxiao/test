# -*- coding:utf-8 -*-
"""
@Time: 2022/9/28 15:41
@Author: zxq
@File: 练习3：9月28日.py
"""
import urllib.request
import urllib.parse
# 练习
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",

}
data = {
    "from": "en",
    "to": "zh",
    "query": "red",
    "simple_means_flag": 3,
    "sign": 207046.510967,
    "token": "ec169ea73b5f5a02275f622a85a34838",
    "domain": "common"
}
info = bytes(urllib.parse.urlencode(data).encode('utf-8'))
requests = urllib.request.Request(url, data=info, headers=headers)
# 添加请求头信息
requests.add_header("Cookie","BIDUPSID=608CA3B10429E9FF21CC9310F863AD5E; PSTM=1663670944; BAIDUID=608CA3B10429E9FF263CE8C434FF16EA:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_PS_PSSID=36543_36459_37358_36885_37486_37403_37273_36569_36789_26350_37284_37363_37467; BA_HECTOR=242g0h2121a40k0ha48h17l31hj4hk519; BAIDUID_BFESS=608CA3B10429E9FF263CE8C434FF16EA:FG=1; ZFY=7oNIsrs:BOnPoKpdPDN4WySBM7ZH:AG6g4DCwZlAzxUEE:C; delPer=0; PSINO=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1664191397,1664191510,1664196710,1664239259; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1664239259; ab_sr=1.0.1_ZGRhODZiYjRjYjFjNjBjMTJjNGM5ZjkxMTRlZTBkZjgyMmIzNjA5YzE2ZDQ2NTdjMjVlZmQ2ZGJjNjQ5NmU5MzQ3ZmYxN2FkN2M1YTkxOGVjZjgzYzViOTc2ZWRiYzg5NTFlMWQ5ZDQxMzkzZTE4OWZiNWFiMzBkYjEwZDBlOTY2ODhiMmY5ZjBiMjkyNWU3YjkzNDQ5MWI0NDNkMTk2OA==")
response = urllib.request.urlopen(requests)
html1 = response.read().decode('utf-8')
print(html1)
