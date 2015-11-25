# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html


#FILES_STORE = "/home/adrian/projects/time_magazine/timecoverspider/output"

class EtsySpiderPipeline(object):
	def process_item(self, item, spider):
		return item

		
class TestPipeline(object):
	pass
	

	
'''
from scrapy.exceptions import DropItem

class PricePipeline(object):

    vat_factor = 1.15

    def process_item(self, item, spider):
        if item['price']:
            if item['price_excludes_vat']:
                item['price'] = item['price'] * self.vat_factor
            return item
        else:
            raise DropItem("Missing price in %s" % item)
'''