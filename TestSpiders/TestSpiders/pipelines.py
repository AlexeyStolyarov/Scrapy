# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import json

class TestspidersPipeline(object):
    def process_item(self, item, spider):

    	return json.dumps(dict(item)) + "\n"
    	cleanr = re.compile('<.*?>')
    	txt =  re.sub(cleanr, '', item)
        return txt