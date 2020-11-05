import scrapy
from urllib.parse import urljoin
from selenium import webdriver
import selenium

class DongmanzhijiaSpider(scrapy.Spider):
    name = 'dongmanzhijia'
    allowed_domains = ['manhua.dmzj.com']
    start_urls = ['https://manhua.dmzj.com/reconglingkaishideyishijieshenghuodisizhang/']
    # start_urls = ['https://manhua.dmzj.com/reconglingkaishideyishijieshenghuodisizhang/94173.shtml#@page=2']

    def __init__(self):
        opt = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        opt.add_experimental_option('prefs', prefs)
        path ='D:\\webdriver\\chrome\\86\\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=path,options=opt)

    def parse(self, response):
        print(self.driver.get(response.url))
        manga_lists = response.xpath('//div[@class="cartoon_online_border"]//a')
        start_url ='https://manhua.dmzj.com/reconglingkaishideyishijieshenghuodisizhang/'
        for manga_list in manga_lists:
            charpter_url = manga_list.xpath('./@href').extract_first()
            next_url = urljoin(start_url,charpter_url)
            print(next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse_manga,
                dont_filter=True
            )
    def parse_manga(self,response):
        print("parse_manga: {%s}" % self.driver.get(response.url))
        page_lists = response.xpath('//div[@class="btmBtnBox"]/select/option')
        print(page_lists)
        for page_list in page_lists:
            print(page_list)