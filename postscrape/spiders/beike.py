import scrapy


class BeikeSpider(scrapy.Spider):
    name = 'beike'
    allowed_domains = ['cd.zu.ke.com']
    start_urls = ['https://cd.zu.ke.com/zufang/gaoxin7/rt200600000001/']

    def parse(self, response):
        div_list = response.xpath('//div[@class="content__list--item"]')
        for div in div_list:
            item = {}
            item['url'] = div.xpath('./a/@href').extract_first()
            item['title'] = div.xpath('./a/@title').extract_first()
            item['price'] = '%s元' % div.xpath('./div[@class="content__list--item--main"]/span/em/text()').extract_first()
            print(item)
            yield item