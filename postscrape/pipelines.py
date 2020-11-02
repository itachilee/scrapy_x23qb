# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pymongo import MongoClient
from gridfs import *
client = MongoClient()
collention = client['x23qb']['xuanhuan']

novel_item = {}
class PostscrapePipeline:
    def open_spider(self, spider):
        """定义items，用来保存每个item"""
        self.items = []

    def process_item(self, item, spider):
        item['spider_name'] = spider.name
        print(item)
        if item['spider_name'] == 'x23qb':
            collention.insert(dict(item))
        self.items.append(item)
        return item


    def close_spider(self, spider):
        """在爬虫结束的时候，将items按照'num'字段排列，并最终合并成一个文件"""
        with open('test.txt', 'w', encoding='utf-8') as f:
            # 所有章节按order字段排序
            self.items.sort(key=lambda i: i['num'])

            for item in self.items:
                print(item['title'])
                f.write("\r\n"+item['title']+"\r\n")
                f.write(item['content'])
