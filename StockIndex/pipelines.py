# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html



class StockindexPipeline(object):
    def process_item(self, item, spider):
        #remove comma from string
        if ',' in item['Value']:  
            item['Value'] = item['Value'].replace(',', '')
        
        #modify index name
        index = item['Index_name'].find('-') + 2
        item['Index_name'] = item['Index_name'][index:]
            
        #save data as csv file    
        with open(r"D:\Stock Market Indexes.csv", 'a') as file:  
            file.write('%s,' %item['Index_name'])
            file.write('%s,' %item['Value'])
            file.write('%s,' %item['Change'])
            file.write('%s\n' %item['Time'])
        return item
