#Scrapy settings for clobot project

BOT_NAME = 'clobot'

SPIDER_MODULES = ['clobot.spiders']
NEWSPIDER_MODULE = 'clobot.spiders'
DEFAULT_ITEM_CLASS = 'clobot.items.ProductItem'

ITEM_PIPELINES = {
                  'clobot.pipelines.InvalidPipeline': 100,
                  'clobot.pipelines.SanitizationPipeline': 900,     
                  }