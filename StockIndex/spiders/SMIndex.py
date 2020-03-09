# -*- coding: utf-8 -*-
import scrapy
from StockIndex.items import StockindexItem


class SmindexSpider(scrapy.Spider):
    name = 'SMIndex'
    allowed_domains = ['finance.yahoo.com'] #containing domains that this spider is allowed to crawl
    start_urls = ['https://finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC',
                  'https://finance.yahoo.com/quote/%5EDJI?p=^DJI',
                  'https://finance.yahoo.com/quote/%5EIXIC?p=^IXIC',
                  'https://finance.yahoo.com/quote/%5ERUT?p=^RUT',
                  'https://finance.yahoo.com/quote/CL=F?p=CL=F',
                  'https://finance.yahoo.com/quote/GC=F?p=GC=F']

    def parse(self, response):
        item = StockindexItem()
        item['Index_name'] = response.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1/text()').extract()[0]     
        item['Value'] = response.xpath("//div/span/text()").extract()[4]
        item['Change'] = response.xpath("//div/span/text()").extract()[5]
        item['Time'] = response.xpath("//div/span/text()").extract()[6]
        
        return item

        

        
        
    
    




