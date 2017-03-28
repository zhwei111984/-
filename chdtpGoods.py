# -*- coding: utf-8 -*-
import scrapy
from huadian.items import HuadianItem

#华电商品需求爬虫
class ChdtpgoodsSpider(scrapy.Spider):
    name = "chdtpGoods"
    allowed_domains = ["chdtp.com.cn"]
    start_urls = ['http://www.chdtp.com.cn/staticPage/ormd/2017/03/22/ormd_906564_321357.html']

    def parse(self, response):
        goodsSelector = response.xpath('//div[@class="main_top main_top_CG"]')
        items = []
        for goods in goodsSelector:
            item = HuadianItem()
            item['name'] = goods.xpath('./div[@class="Procurement_of_goods"]/table/tr[@bgcolor="#FFFFFF"]/td[2]/text()').extract()
            item['model'] = goods.xpath('./div[@class="Procurement_of_goods"]/table/tr[@bgcolor="#FFFFFF"]/td[3]/text()').extract()
            item['unit'] = goods.xpath('./div[@class="Procurement_of_goods"]/table/tr[@bgcolor="#FFFFFF"]/td[4]/text()').extract()
            item['numbers'] = goods.xpath('./div[@class="Procurement_of_goods"]/table/tr[@bgcolor="#FFFFFF"]/td[5]/text()').extract()
            item['classify'] = goods.xpath('./div[@class="headline"]/dl/dt/text()').extract()
            item['buyer'] = goods.xpath('./div[@class="headline"]/dl/dd/span/a/text()').extract()
            item['date'] =  goods.xpath('./div[@class="headline"]/dl/dd//text()[2]').extract()
            items.append(item)
        return items
    
