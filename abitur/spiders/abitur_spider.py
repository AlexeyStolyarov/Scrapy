# -*- coding:utf8 -*-

import re
import time

from abitur.items import AbiturItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Compose
from scrapy.contrib.loader.processor import MapCompose
from scrapy.contrib.loader.processor import TakeFirst
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy.selector import HtmlXPathSelector

class AbiturLoader(XPathItemLoader):
    default_input_processor = MapCompose(lambda s: re.sub('\s+', ' ', s.strip()))
    default_output_processor = TakeFirst()

class AbiturSpider(CrawlSpider):

    name = "abitur"
    allowed_domains = ["www.amadeusmusic.ru"]
    start_urls = ["http://www.amadeusmusic.ru/ID_140_232_V0.html"]

    rules = (
             Rule(SgmlLinkExtractor(allow=('ID.+')), follow=True),
             Rule(SgmlLinkExtractor(allow=('UID.+')), callback='parse_item'),
             )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)

        l = AbiturLoader(AbiturItem(), hxs)
        l.add_xpath('name', './/*[@id="cart_quantity"]/h1/text()')
        l.add_xpath('price', './/*[@id="cart_quantity"]/p[1]/span/text()')
        return l.load_item()
