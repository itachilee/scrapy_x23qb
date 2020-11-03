import scrapy
from postscrape.items import SplashItem
import json
import re


class SplashSpider(scrapy.Spider):
    name = 'splash'
    allowed_domains = ['unsplash.com/']
    start_urls = [
        'https://unsplash.com/napi/search/photos?query=splash&xp=feedback-loop-v2%3Aexperiment&per_page=20&page=1']

    def parse(self, response):
        jdict = json.loads(response.body)
        total_pages = int(jdict['total_pages'])
        results = jdict['results']
        for each in results:
            image_url = each['urls']['regular']
            re.sub(r'https', 'http', image_url)
            item = SplashItem()
            item['title'] = each['alt_description']
            item['image_urls'] = [image_url]
            yield item
        pn = int(response.url.split('=')[-1])
        if pn < total_pages:
            next_pn = int(pn + 1)
            print('共{%d}页，已下载{%d}页' % (total_pages, pn))
            next_url = 'https://unsplash.com/napi/search/photos?query=splash&xp=feedback-loop-v2%3Aexperiment&per_page=20&page=' + str(
                next_pn)
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                dont_filter=True
            )
