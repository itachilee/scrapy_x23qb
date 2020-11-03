import scrapy
import re


class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com/top250']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movie_list:
            item = {}
            item['title'] = movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract_first()
            item['eng_title'] = re.sub(r'[\xa0]?', '',
                                       movie.xpath('.//div[@class="hd"]/a/span[2]/text()').extract_first())
            if movie.xpath('.//div[@class="hd"]/a/span[3]/text()').extract_first() is not None:
                item['nick_title'] = re.sub(r'[\xa0]?', '',
                                            movie.xpath('.//div[@class="hd"]/a/span[3]/text()').extract_first())
            else:
                item['nick_title'] = movie.xpath('.//div[@class="hd"]/a/span[3]/text()').extract_first()

            print(item)
            yield
