# -*- coding: utf-8 -*-

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from etsy_spider.items import EtsySpiderItem
import re

import logging
logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG)


logger = logging.getLogger('my logger')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('./scrapy.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
formatter =logging.Formatter(u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add the handlers to logger
#logger.addHandler(ch)
logger.addHandler(fh)


class Spider1Spider(CrawlSpider):
	name = 'spider1'
	allowed_domains = ['etsy.com']
	start_urls = ['https://www.etsy.com/c/art-and-collectibles/collectibles/coins?ref=catnav-891']

    #rules = (
    #    Rule(SgmlLinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    #)
	
	def parse_item(self, response):
		hxs = HtmlXPathSelector(response)
		i = EtsySpiderItem()
		
		#i['image_urls'] = Field()
		#i['images'] = Field()
		#i['dealer'] = Field()
		i['title'] = hxs.select(".//*[@id='listing-page-cart-inner']/h1/span/text()").extract()
		
		#i['description']  = Field()
		i['price'] = hxs.select(".//*[@id='listing-price']/span/span[2]/text()").extract()
		#i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
		tmp = ''
		tmp = ' '.join(hxs.select(".//*[@id='description-text']/text()").extract())
		tmp = re.sub(r'\n','', tmp)
		i['description'] = re.sub(r'^\s+|\s+$','', tmp)
		logger.debug(i)
    #    return i
	rules = (
             Rule(SgmlLinkExtractor(allow=r'/page\=\d/'), follow=True),
             Rule(SgmlLinkExtractor(allow=('.+listing.+')), callback='parse_item'),
             )
