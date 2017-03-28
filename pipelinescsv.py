# -*- coding: utf-8 -*-
import csv
import codecs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HuadianPipeline(object):
    def process_item(self, item, spider):
        csvfile = file('huadian.csv', 'wb')
        csvfile.write(codecs.BOM_UTF8)
        writer = csv.writer(csvfile)
        writer.writerow(['产品名称', '规格型号', '单位','数量','采购单位','发布时间','询价单名称'])
        data = [item['name'],item['model'],item['unit'],item['numbers'],item['buyer'],
                item['date'],item['classify'] ]
        for i in data:
            writer.writerow(i)
        csvfile.close()
      
        
