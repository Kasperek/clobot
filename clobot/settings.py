# Scrapy settings for clobot project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'clobot'

SPIDER_MODULES = ['clobot.spiders']
NEWSPIDER_MODULE = 'clobot.spiders'
DEFAULT_ITEM_CLASS = 'clobot.items.ProductItem'

ITEM_PIPELINES = ['clobot.pipelines.ProductPipeline']


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'clobot (+http://www.yourdomain.com)'
