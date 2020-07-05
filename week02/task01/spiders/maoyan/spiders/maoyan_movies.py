import scrapy
from maoyan.items import MaoyanItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'maoyan_movies'
    allowed_domains = ['maoyan.com']
    # 起始URL列表
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    # 自定义请求网址
    # def start_requests(self):
    #     for i in range(0, 10):
    #         url = f'https://movie.douban.com/top250?start={i*25}'
    #         yield scrapy.Request(url=url, callback=self.parse)
    #         # url 请求访问的网址
    #         # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
    #         # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        # print(response.text)
        print(response.url)
        movie_selector_generator = (movie for movie in Selector(
            response=response).xpath('//dl[@class="movie-list"]').xpath('//dd'))
        for i in range(10):
            item = MaoyanItem()
            movie = next(movie_selector_generator)
            film_title = movie.xpath('./div[2]/a/text()').extract()
            item['film_title'] = film_title
            print(film_title)
            movie_type = movie.xpath(
                './div[1]/div[2]/a/div/div[2]/text()').extract()[-1].strip()
            item['movie_type'] = movie_type
            print(movie_type)
            plan_date = movie.xpath(
                './div[1]/div[2]/a/div/div[4]/text()').extract()[-1].strip()
            item['plan_date'] = plan_date
            print(plan_date)
            yield item
