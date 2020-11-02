import scrapy
from urllib.parse import urljoin
import re
from postscrape.items import NovelItem
class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['www.booktxt.net']
    start_urls = ['https://www.booktxt.net/8_8455']

    def parse(self, response):
        novel_list = response.xpath('//div[@id="list"]/dl/dd')
        for novel in novel_list:
            chapter_url= novel.xpath('./a/@href').extract_first()
            url =urljoin('https://www.booktxt.net/8_8455/',chapter_url)
            yield scrapy.Request(url ,
                                 callback=self.novel_parse,
                                 dont_filter=True)


    def novel_parse(self,response):
        item= NovelItem()

        item['title'] = response.xpath(' //div[@class="bookname"]/h1/text()').extract_first()
        item['num'] = int(re.findall(r'\d+\.?\d*',item['title'])[0])
        item['content'] = re.sub(r'[\t\r\n]', '', response.xpath('string(//div[@id="content"])').extract_first())
        yield item