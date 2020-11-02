import scrapy
from postscrape.items import SplashItem
import json
import re
class SplashSpider(scrapy.Spider):
    name = 'splash'
    allowed_domains = ['unsplash.com/']
    start_urls = ['https://unsplash.com/napi/search/photos?query=splash&xp=feedback-loop-v2%3Aexperiment&per_page=20&page=2']

    def parse(self, response):
        jdict = json.loads(response.body)
        total_pages = jdict['total_pages']
        total = jdict['total']
        results = jdict['results']
        print(results)
        print(total_pages)
        for each in results:
            image_url = each['urls']['regular']
            re.sub(r'https','http',image_url)
            item = SplashItem()
            item['title'] = each['alt_description']
            item['image_urls'] = [image_url]
            yield item
