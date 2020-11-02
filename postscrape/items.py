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
    image_urls =scrapy.Field()
    images =scrapy.Field()
    title =scrapy.Field()