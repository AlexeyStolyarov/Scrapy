# Scrapy settings for etsy_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'etsy_spider'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['etsy_spider.spiders']
NEWSPIDER_MODULE = 'etsy_spider.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

#ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}