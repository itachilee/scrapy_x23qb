import scrapy
from urllib.parse import urljoin
from selenium import webdriver
import selenium

class DongmanzhijiaSpider(scrapy.Spider):
    name = 'dongmanzhijia'
    allowed_domains = ['manhua.dmzj.com']
    # start_urls = ['https://manhua.dmzj.com/reconglingkaishideyishijieshenghuodisizhang/']
    start_urls = ['https://www.dmzj.com/view/jinglingzhidan/59638.html#@page=1']

    def __init__(self):
        opt = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        opt.add_experimental_option('prefs', prefs)
        path ='D:\\webdriver\\chrome\\86\\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=path,options=opt)

    def parse(self, response):
        print(self.driver.get(response.url))
        item_lists = self.driver.find_elements_by_xpath('//div[@class="btmBtnBox"]/select/option')
        for item in item_lists:
            print(item.get_attribute('value'))
            print(item.text)
        # manga_lists = response.xpath('//div[@class="cartoon_online_border"]//a')
        # start_url ='https://manhua.dmzj.com/reconglingkaishideyishijieshenghuodisizhang/'
        # for manga_list in manga_lists:
        #     charpter_url = manga_list.xpath('./@href').extract_first()
        #     next_url = urljoin(start_url,charpter_url)
        #     yield scrapy.Request(
        #         next_url,
        #         callback=self.parse_manga,
        #         dont_filter=True
        #     )

    # def parse_manga(self,response):
    #     print("parse_manga: {%s}" % self.driver.get(response.url))
    #     page_lists = response.xpath('//div[@class="btmBtnBox"]/select/option')
    #     print(page_lists)
    #     for page_list in page_lists:
    #         print(page_list)