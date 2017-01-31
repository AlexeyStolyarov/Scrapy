# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
#from myproject.items import MyprojectItem

class MySpider(CrawlSpider):
    name = "example"
    allowed_domains = ["bash.im"]
    start_urls = ['http://bash.im/']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        #Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),
		## https://doc.scrapy.org/en/latest/topics/link-extractors.html#topics-link-extractors
        Rule(LinkExtractor(allow=(r'http://bash.im/index/\d+')),follow=True, callback='parse_item'),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        #Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
    )

    def parse_item(self, response):
        print response
        return
##        self.logger.info('Hi, this is an item page! %s', response.url)
#        item = scrapy.Item()
##        item = MyprojectItem()
##        item['title'] = response.xpath(".//*[@id='body']/div[*]/div[2]").extract()
 #       item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
 #       item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
 #       item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
##        return item