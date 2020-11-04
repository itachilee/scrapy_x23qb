import scrapy
import re


class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com/top250']
    start_urls = ['https://movie.douban.com/top250?start=0']

    def parse(self, response):
        movie_list = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movie_list:
            item = {}
            item['title'] = movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract_first()
            item['eng_title'] = re.sub(r'[\xa0\uc2e0\u062c\ub3c4]?', '',
                                       movie.xpath('.//div[@class="hd"]/a/span[2]/text()').extract_first())
            if movie.xpath('.//div[@class="hd"]/a/span[3]/text()').extract_first() is not None:
                item['nick_title'] = re.sub(r'[\xa0\uc2e0\u062c\ub3c4]?', '',
                                            movie.xpath('.//div[@class="hd"]/a/span[3]/text()').extract_first())
            else:
                item['nick_title'] = movie.xpath('.//div[@class="hd"]/a/span[3]/text()').extract_first()

            item['quote'] = re.sub(r'[\xa0\uc2e0\u062c\ub3c4]?', '',
                                   movie.xpath('.//div[@class="bd"]/p[@class="quote"]/span/text()').extract_first())

            item['desc'] = movie.xpath('string(.//div[@class="bd"]/p[1]/text())').extract_first()
            yield item
        try:
            current_at = int(response.url.split('=')[-1])
            next_at = current_at + 25
            print(next_at)
        except RuntimeError:
            print('转换出错')
        if current_at < 225:
            next_url = 'https://movie.douban.com/top250?start=' + str(next_at)
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                dont_filter=True
            )
