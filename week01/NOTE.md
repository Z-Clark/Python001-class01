Week01 学习笔记 07.03

**1.提交作业流程及基本git操作**

```python
fork
clone
# 在没有git分支的目录git clone
git clone
# cd 到作业目录
vim homework.py
vim NOTE.md
git add .
git commit -m ""
git push -u origin master
```

**2.打印文件时的编码问题**

UnicodeEncodeError: 'gbk' codec can't encode character '\xee'

解决办法：

先用 GBK 编码，加个 ignore 丢弃错误的字符，然后再解码。

eg: print(response.text.encode('gbk', 'ignore').decode('gbk'))
**（更正）一劳永逸的解决办法：**

新建系统变量，变量名为：PYTHONIOENCODING，值为：UTF8

**3.终端运行python文件**

改变终端路径至目标python文件所在文件夹，输入 python 文件名.py 即可。

**4.头部header重要内容

- Request URL

- 请求方式 Request Method

- Status Code: 1xx 信息响应, 2xx成功响应, 3xx重定向, 4xx客户端响应, 5xx服务端响应

- cookie：包括用户名 密码等验证信息

- User-agent：客户端浏览器，反爬虫

  爬虫一定要模拟user-agent、cookie

**4.一些小技巧操作**

- 终端输入
  dir(math) -- 可以看到库所支持的所有方法
  help(math) -- 可以看到函数参数

- XPath路径注意简化


- 访问网站时，如有验证中心，可在浏览器手动验证，注意换cookie;
- 访问多网页时，注意添加引入sleep包，加入等待时间sleep(5)等; 
- shift + 回车 ：可以运行选择部分的代码

**5.Scrapy框架**

- 框架结构图

![img](https://static001.geekbang.org/resource/image/e2/21/e2954a386344f0c1a065b4e0bc384a21.png)

- Scrapy组件

![屏幕截图(6)](C:\Users\90927\Pictures\Screenshots\屏幕截图(6).png)

- scrapy基本操作

```python
## 生成起始项目
scrapy startproject spiders # spiders是项目文件夹名
cd spiders
cd spiders/
scrapy genspider maoyan_movies maoyan.com # 生成爬虫文件maoyan_movies
scrapy crawl maoyan_movies # 终端运行爬虫
```



- scrapy爬虫

```python
name = 'douban' # 爬虫的名字

import scrapy # 不光导入scrapy的一系列功能，还有其他的修改的设置等附带内容也会随之导入

allowed_domains = ['movie.douban.com'] # 限制爬虫爬取的域名范围

start_urls = ['https://movie.douban.com/top250'] # 第一次请求的域名（获取头部信息）

def parse(self, response) # 爬取内容的方法，往里填写爬虫逻辑

scrapy crawl douban # 终端运行scrapy 爬虫,douban是爬虫名字

settings.py # 头文件、等待时间等设置
items.py # 设置存储的各项内容
pipelines.py # 设置不同的存储介质，将items存入
```

**6.XPath路径**

```python
## 这些方式覆盖80%的XPath用法
## 四种XPath搜索方法
//div[@id = "hd"] 表示从上到下搜索匹配的div，更高效
/div 表示从第一个div搜索
./ 表示从当前位置开始找
../ 表示从当前位置的上一级开始找

## XPath取内容
./a/span/text() # 后面加上/text()

## XPath取属性
./a/@href # 后面加上 @属性名 

## XPath调试方法
1.在浏览器搜索路径调试
2.利用print语句输出匹配结果

## XPath搜索结果处理
title.extract() # 释放所有匹配结果
title.extract_first() # 释放第一个匹配结果
title.extract_first().strip() # 去除第一个匹配结果的前后空格
```

**7.yield**

yield相当于return， 但更灵活，可以返回单独值，不考虑返回类型，且可以一条一条地返回，而return是一次性返回