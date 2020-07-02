学习笔记

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

终端输入
dir(math) -- 可以看到库所支持的所有方法
help(math) -- 可以看到函数参数

XPath路径注意简化

访问网站时，如有验证中心，可在浏览器手动验证，注意换cookie; 访问多网页时，注意添加引入sleep包，加入等待时间sleep(5)等; 