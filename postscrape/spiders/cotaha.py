import scrapy


class CotahaSpider(scrapy.Spider):
    name = 'cotaha'
    allowed_domains = ['api.ce-cotoha.com']
    start_urls = ['https://api.ce-cotoha.com/']

    def __init__(self):
        self.token = 'Bearer YrFbUcAZAk25qMc8kk5FN132QARq'

    def parse(self, response):
        pass

