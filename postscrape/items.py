# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PostscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    copy_right = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    category = scrapy.Field()
    status = scrapy.Field()
    desc = scrapy.Field()
    last_chapter = scrapy.Field()
    spider_name = scrapy.Field()


class NovelItem(scrapy.Item):
    num = scrapy.Field()
    content = scrapy.Field()
    title = scrapy.Field()
    spider_name = scrapy.Field()


class SplashItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    title = scrapy.Field()
    spider_name = scrapy.Field()


class StockShItem(scrapy.Item):
    rank = scrapy.Field()
    板块 = scrapy.Field()
    公司家数 = scrapy.Field()
    平均价格 = scrapy.Field()
    平均涨跌额 = scrapy.Field()
    平均涨跌幅 = scrapy.Field()
    总手 = scrapy.Field()
    总成交金额 = scrapy.Field()
    板块 = scrapy.Field()
    涨跌额 = scrapy.Field()
    涨跌幅 = scrapy.Field()
