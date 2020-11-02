import scrapy
import re
from w3lib.html import remove_tags
from postscrape.items import PostscrapeItem

class X23qbSpider(scrapy.Spider):
    name = 'x23qb'
    allowed_domains = ['x23qb.com/']
    start_urls = ['https://www.x23qb.com/xuanhuan/1/']

    def parse(self, response):
        novel_list = response.xpath('//div[@id="sitebox"]/dl')
        for novel in novel_list:
            item = PostscrapeItem()
            item['copy_right'] = novel.xpath('./dt[1]/span/text()').extract_first()
            item['title'] = novel.xpath('./dd[1]//a/text()').extract_first()
            item['date'] = novel.xpath('./dd[1]//span/text()').extract_first()
            item['category'] = novel.xpath('./dd[2]//span[1]/text()').extract_first()
            item['status'] = novel.xpath('./dd[2]//span[2]/text()').extract_first()
            item['desc'] = novel.xpath('./dd[3]/text()').extract_first()
            item['last_chapter'] = novel.xpath('./dd[4]//a/text()').extract_first()
            yield item
        page_num = response.url.split('/')[-2]
        print(page_num)
        if int(page_num) < 110:
            # print(response.url)
            next_url = 'https://www.x23qb.com/xuanhuan/' + str(int(response.url.split('/')[-2]) + 1) + '/'
            # print(next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                dont_filter=True
            )
