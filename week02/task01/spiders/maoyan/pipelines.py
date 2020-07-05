# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import logging

dbInfo = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'rootroot',
    'db': 'test'
}


class MaoyanPipeline:
    # def process_item(self, item, spider):
    #     return item

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        try:
            sqls = [
                f'insert into film_list (film_title,movie_type,plan_date) values ({item["film_title"]}, {item["movie_type"]}, {item["plan_date"]})']
            db = ConnDB(dbInfo, sqls)
            db.run()
        except Exception as e:
            logging.warn(f'save data fail for {e}')

        return item


result = []


class ConnDB(object):
    def __init__(self, dbInfo, sqls):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.sqls = sqls

        # self.run()

    def run(self):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )
        # 游标建立的时候就开启了一个隐形的事物
        cur = conn.cursor()
        try:
            for command in self.sqls:
                cur.execute(command)
                result.append(cur.fetchone())
            # 关闭游标
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        # 关闭数据库连接
        conn.close()
