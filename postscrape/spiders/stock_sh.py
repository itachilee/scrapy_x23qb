import scrapy
from selenium import webdriver
import selenium
from time import sleep

class StockShSpider(scrapy.Spider):
    name = 'stock_sh'
    allowed_domains = ['q.stock.sohu.com']
    start_urls = ['https://q.stock.sohu.com/cn/bk.shtml']

    def __init__(self):
        opt = webdriver.ChromeOptions()
        '''
            设置不显示图片
        '''
        prefs = {"profile.managed_default_content_settings.images": 2}
        opt.add_experimental_option('prefs', prefs)
        '''
            驱动地址
        '''
        path = 'D:\\webdriver\\chrome\\86\\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=path, options=opt)

    def parse(self, response):
        self.driver.get(response.url)
        sleep(3)
        tr_list = self.driver.find_elements_by_xpath('//table[@id="BIZ_MS_pllist"]/tbody/tr')
        for tr in tr_list:
            item = {}
            info = tr.text
            info_list = info.split(' ')
            if len(info_list) > 11:
                item['排名'] = info_list[0]
                item['板块'] = info_list[1]
                item['公司家数'] = info_list[2]
                item['平均价格'] = info_list[3]
                item['平均涨跌额'] = info_list[4]
                item['平均涨跌幅'] = info_list[5]
                item['总手'] = info_list[6]
                item['总成交金额'] = info_list[7]
                item['领涨股'] = info_list[8]
                item['涨跌额'] = info_list[9]
                item['涨跌幅'] = info_list[10]
            yield item

        self.driver.close()
