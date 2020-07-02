# 爬取电影页面详细信息，包括电影名称、上映时间，并以UTF-8 字符集保存到 csv 格式的文件中
# 这里采用Xpath来进行搜索，而非使用BeautifulSoup进行标签匹配

import requests
import lxml.etree  # 使用XPath
import pandas as pd

# 模拟浏览器访问
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
cookie = 'uuid_n_v=v1; uuid=F97222B0B76811EA9736CB82F1E06989920248FF2A224C3CBF94A7A34351517D; mojo-uuid=2b4fed65a835e681e1fdb005bddb1e46; _lxsdk_cuid=172eef93ae8c8-0eeb2f133b8fa6-4353760-144000-172eef93ae8c8; _lxsdk=F97222B0B76811EA9736CB82F1E06989920248FF2A224C3CBF94A7A34351517D; _csrf=8c54da97c327305eb0b03d703906e01ed4ce97171f3fef05b4da8c7dfc918800; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593147210,1593223737; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593225630; __mta=121412407.1593147210586.1593225614673.1593225630337.5; _lxsdk_s=172f3cff427-05e-d5e-ef5%7C%7C1'

header = {'user-agent': user_agent, 'Cookie': cookie}

# 猫眼电影网址
myurl = 'https://maoyan.com/films/1250952'

# 完整网页源代码内容
response = requests.get(myurl, headers=header)

# xml化处理
selector = lxml.etree.HTML(response.text)

# 利用XPath搜索电影名称、上映日期
film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
print(film_name)
plan_date = selector.xpath(
    '/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
print(len(plan_date))

# 以UTF-8 字符集保存到 csv 格式的文件中
mylist = [film_name, plan_date]
print(mylist)
movie1 = pd.DataFrame(data=mylist)
movie1.to_csv('Python001-class01/week01/example01/maoyan_1.csv',
              encoding='utf8', index=False, header=False)
