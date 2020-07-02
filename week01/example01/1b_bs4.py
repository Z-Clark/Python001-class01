# 使用BeautifulSoup解析网页，获取猫眼电影链接

import requests
from bs4 import BeautifulSoup as bs

# 模拟浏览器访问
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
cookie = '__mta=208417709.1592895912492.1592902918645.1592903952867.7; uuid_n_v=v1; uuid=DF9CCBB0B51F11EA801551553EAD9849A9C6A4B3E2894835A13DFBE0903318F2; _csrf=b440c76ad9bd8b530488f522785e6cf7af43ac1e907b9196a84bc71857d4234e; _lxsdk_cuid=172dffeb93ec8-0d64910ea0f05a-143e6257-1fa400-172dffeb93ec8; mojo-uuid=6a2c8527c33ed9dd8462351a67bb364e; mojo-session-id={"id":"5fa649bfa4a5fb40547b9af2b7ae5a30","time":1592898021553}; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172e0281287bdf-06e09e70bab7de-2076244f-546797-172e0281288c3f%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22172e0281287bdf-06e09e70bab7de-2076244f-546797-172e0281288c3f%22%7D; _lxsdk=DF9CCBB0B51F11EA801551553EAD9849A9C6A4B3E2894835A13DFBE0903318F2; lt=sbcAoSSv2aNOkmQO1M30XtzxY4oAAAAA5woAAM42swSU-Amm1PnUAOMGoyjjYbuzAnq3nio6jK_ArkGALUH-whiVT6KsP7yiYWj32g; lt.sig=ytlNcmJAcMmZ5ZqM84NQiRBdoqM; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592906608,1592906937,1592906948,1592906968; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1592906968; __mta=208417709.1592895912492.1592903952867.1592906969162.8; mojo-trace-id=50; _lxsdk_s=172e01ee84e-47c-6be-c2b%7C%7C99'

header = {'user-agent': user_agent, 'Cookie': cookie}

# 猫眼电影网址
myurl = 'https://maoyan.com/films?showType=3'

# 完整网页源代码内容
response = requests.get(myurl, headers=header)

# 使用BeautifulSoup解析网页
bs_info = bs(response.text, 'html.parser')

# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
# 只获取前十部电影名字及链接
cnt = 10

for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}):
    # 获取电影名字
    print(tags.get('title'))
    for atag in tags.find_all('a'):
        # 获取链接
        url = 'https://maoyan.com/' + atag.get('href')
        print(url)
    cnt -= 1
    if cnt <= 0:
        break
