'''
Week01 作业1: 使用requests、bs4库，爬取猫眼电影的前十个电影名称、电影类型和上映时间，并以UTF-8字符集保存到csv格式的文件中
'''
# 爬取电影页面详细信息，包括电影名称、上映时间，并以UTF-8 字符集保存到 csv 格式的文件中

import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd

# 模拟浏览器访问
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
cookie = 'uuid_n_v=v1; uuid=C7D05710BAB811EAA3E73598CBDBCCBE0BCFFA39D6EB4BEAAA51C9D13E0B9DE4; mojo-uuid=38a9a44391b3aea5f2f8bcb326115c5f; mojo-trace-id=1; mojo-session-id={"id":"08f3c68ddce3a0a92acd2c04aecbe21f","time":1593511338995}; _lxsdk_s=17304ad60b3-7e7-c3f-403%7C2902577504%7C2; _lxsdk_cuid=172fb119180c8-054a25ec59fcc8-79657967-144000-172fb1191800; _lxsdk=C7D05710BAB811EAA3E73598CBDBCCBE0BCFFA39D6EB4BEAAA51C9D13E0B9DE4; _csrf=32dcbdb3045f2be1b0e5543011ec9882b18efb089882e50f07405b4ee0ab0b8b; __mta=222190247.1593511339532.1593511339532.1593511339532.1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593506403,1593509061,1593509384,1593511320;Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593511339; '
header = {'user-agent': user_agent, 'Cookie': cookie}

# 猫眼电影网址
myurl = 'https://maoyan.com/films?showType=3'

# 完整网页源代码内容
response = requests.get(myurl, headers=header)
# print(response.text)

# 使用BeautifulSoup解析网页
bs_info = bs(response.text, 'html.parser')

movie_list = []
cnt = 0

for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    # 获取电影名字
    film_name = tags.find('span', attrs={'class': 'name'}).text
    # print(film_name)
    # 获取电影类型
    hover_tags = tags.find_all('span', attrs={'class': 'hover-tag'})
    for tag in hover_tags:
        # 利用replace去除多余空格和换行，并用split根据冒号分片，取第二部分
        if tag.text == "类型:":
            movie_type = tag.parent.text.replace(
                ' ', '').replace('\n', '').split(':')[1]
            # print(movie_type)
        if tag.text == "上映时间:":
            plan_date = tag.parent.text.replace(
                ' ', '').replace('\n', '').split(':')[1]
            # print(plan_date)
    movie_list.append([film_name, movie_type, plan_date])
    sleep(5)
    cnt += 1
    if cnt >= 10:
        break

mylist = movie_list
# print(movie_list)
movie1 = pd.DataFrame(data=mylist)
movie1.to_csv('week01/task01/maoyan_top102.csv',
              encoding='utf-8', index=False, header=False)
