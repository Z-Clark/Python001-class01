1. Week02 学习笔记

**1.异常捕获**

所有内置的非系统退出的异常都派生自 Exception 类

```python
gennumber = (i for i in range(0, 2))

# 包括异常
try:# 包括产生异常的过程
    print(next(gennumber))
except StopIteration:# 捕获指定的异常
    print('最后一个元素')
```

**2.异常处理机制的原理**

- 异常也是一个类
- 异常捕获过程：

  1. 异常类把错误消息打包到一个对象
  2. 然后该对象会自动查找到调用栈
  3. 直到运行系统找到明确声明如何处理这些类异常的位置
- 所有异常继承自BaseException（自定义异常必须继承自Exception类）
- Traceback 显示了出错的位置，显示的顺序和异常信息对象传播的方向是相反的

**3.异常信息与异常捕获**

- 异常信息在Traceback信息的最后一行，有不同的类型
- 捕获异常可以使用try...except语法
- try...except支持多重异常处理

常见的异常类型主要有：

1. LookupError下的IndexError和KeyError
2. IOError
3. NameError
4. TypeError
5. AttributeError
6. ZeroDivisionError

```python
Exception # 捕获所有的异常
try:
    1/0
except Exception as e:
    print(e) # 输出异常信息e

## 自定义异常模板
class UserInputError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo
    def __str__(self):
        return self.errorinfo
    
userinput = 'a'

try:
    if (not userinput.isdigit()):
        raise UserInputError('用户输入错误')
except UserInputError as ue:
    print(ue) # 输出异常信息
finally:# 不管是否抛出异常，都需要进行的操作
    del userinput # 释放错误输入所占的内存
    
## 文件读取（更优雅的写法）
with open('a.txt', encoding='utf8') as file:
    data = file.read()
```

4.mysql

```python
启动服务并登录
net start mysql
mysql -u root -p
Password:bfQ<o6fSuy?g

# pymysql
# 一般流程
# 开始-创建connection-获取cursor-CRUD(查询并获取数据)-关闭cursor-关闭connection-结束
import pymysql

conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       password = 'rootroot',
                       database = 'test',
                       charset = 'utf8mb4'
                        )

# 获得cursor游标对象
con1 = conn.cursor()

# 操作的行数
count = con1.execute('select * from tb1;')
print(f'查询到 {count} 条记录')


# 获得一条查询结果
result = con1.fetchone()
print(result)

# 获得所有查询结果
print(con1.fetchall())

con1.close()
conn.close()

# 执行批量插入
# values = [(id,'testuser'+str(id)) for id in range(4, 21) ]
# cursor.executemany('INSERT INTO '+ TABLE_NAME +' values(%s,%s)' ,values)
```

**5.反爬虫**

反爬虫根据两点工作：

- 根据爬虫的基本请求
- 根据爬虫的行为

浏览器的基本行为

- 带http头信息：如User-Agent、Referer等
- 带cookies（包含加密的用户名、密码验证信息）

**6.反反爬虫**

模拟浏览器头部信息（利用fake-useragent包）

```python
from fake_useragent import UserAgent
ua = UserAgent(verify_ssl=False)
ua.random # 随机返回头部信息，推荐使用
```

cookies验证

```python
# http 协议的 GET 方法
import requests
r = requests.get('https://github.com')
# http 协议的 POST 方法
import requests
# 网址 + /post
r = requests.post('http://httpbin.org/post', data = {'key':'value'})

## 在同一个 Session 实例发出的所有请求之间保持 cookie
s = requests.Session()
# key: sessioncookie, value: 123456789
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text) # '{"cookies": {"sessioncookie": "123456789"}}'

## 也可以使用上下文管理器精简
with requests.Session() as s:
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')

#### 用request模拟获取cookie并POST登录
import time
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
# 模拟头部：User-Agent, Referer
headers = {
'User-Agent' : ua.random,
'Referer' : 'https://accounts.douban.com/passport/login_popup?login_source=anony'
}

s = requests.Session()
# 会话对象：在同一个 Session 实例发出的所有请求之间保持 cookie， 
# 期间使用 urllib3 的 connection pooling 功能。
# 向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。
login_url = 'https://accounts.douban.com/j/mobile/login/basic'

# 模拟用户提交表单form_data，注意要和浏览器完全相同
form_data = {
'ck':'',
'name':'15055495@qq.com',
'password':'',
'remember':'false',
'ticket':''
}    
# post数据前获取cookie
pre_login = 'https://accounts.douban.com/passport/login'
pre_resp = s.get(pre_login, headers=headers)
# post请求
response = s.post(login_url, data=form_data, headers=headers, cookies=s.cookies)

# 模拟浏览器行为，点击、填写表单
from selenium import webdriver
import time
try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html
    
    browser.get('https://www.douban.com')
    time.sleep(1)

    browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
    btm1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
    btm1.click()

    browser.find_element_by_xpath('//*[@id="username"]').send_keys('15055495@qq.com')
    browser.find_element_by_id('password').send_keys('test123test456')
    time.sleep(1)
    browser.find_element_by_xpath('//a[contains(@class,"btn-account")]').click()

    cookies = browser.get_cookies() # 获取cookies
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:    
    browser.close()
    
# 大小文件下载    
########## 小文件下载：
import requests
image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
r = requests.get(image_url)
with open("python_logo.png",'wb') as f:
    f.write(r.content)

############# 大文件下载：
# 如果文件比较大的话，那么下载下来的文件先放在内存中，内存还是比较有压力的。
# 所以为了防止内存不够用的现象出现，我们要想办法把下载的文件分块写到磁盘中。
import requests
file_url = "http://python.xxx.yyy.pdf"
r = requests.get(file_url, stream=True)
with open("python.pdf", "wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            pdf.write(chunk)
```

**7.一些小操作**

- scrapy执行时不打印工作日志

```python
scrapy crawl httpbin --nolog # 不打印工作日志，只有输出
```

