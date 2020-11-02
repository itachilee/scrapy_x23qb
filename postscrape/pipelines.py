# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pymongo import MongoClient
from gridfs import *
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import re

client = MongoClient()
collention = client['x23qb']['xuanhuan']

novel_item = {}


class PostscrapePipeline:
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        item['spider_name'] = spider.name
        if item['spider_name'] == 'x23qb':
            collention.insert(dict(item))
        self.items.append(item)
        return item

    def close_spider(self, spider):
        if spider.name == 'novel':
            """在爬虫结束的时候，将items按照'num'字段排列，并最终合并成一个文件"""
            with open('test.txt', 'w', encoding='utf-8') as f:
                # 所有章节按num字段排序
                self.items.sort(key=lambda i: i['num'])

                for item in self.items:
                    print(item['num'])
                    f.write("\r\n" + item['title'] + "\r\n")
                    f.write(item['content'])


class SplashPipeline(ImagesPipeline):

    # 发生图片下载请求
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']  # 通过上面的meta传递过来item
        file_name = item['title']
        # 过滤windows符号
        file_name = re.sub(r'[？\\*|“<>:/]', '', file_name)
        file_name += '.jpg'
        # 分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
        filename = u'{0}/{1}'.format('splash', file_name)
        return filename
