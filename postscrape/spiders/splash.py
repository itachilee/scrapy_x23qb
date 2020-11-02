import scrapy
from postscrape.items import SplashItem

class SplashSpider(scrapy.Spider):
    name = 'splash'
    allowed_domains = ['unsplash.com/']
    start_urls = ['https://unsplash.com/']

    def parse(self, response):
        for i in range(5):
            item = SplashItem()
            item['image_urls'] = ['http://images.unsplash.com/photo-1494967990034-6a28085f9ed0?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb']
            item['title'] = "test"
            yield item
