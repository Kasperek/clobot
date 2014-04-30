from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from clobot.items import ProductItem

class MrPorterSpider(CrawlSpider):
    
    name = "mrporter"
    allowed_domains = ["mrporter.com"]
    start_urls = ["http://www.mrporter.com/"]
    rules = (
             Rule(SgmlLinkExtractor(allow=('/product/\d+')), callback='parse_product'),
             Rule(SgmlLinkExtractor(allow=('/Shop/Clothing/'), deny=('\?'))),
             )
    
    def parse_product(self, response):
        sel = Selector(response)
        print(response)
        product = ProductItem()
        product['url'] = response.url
        product['name'] = sel.xpath("//meta[@property='og:title']/@content").extract()
        product['image'] = sel.xpath("//meta[@property='og:image']/@content").extract()
        product['brand'] = product['name'][0].split(' -')[0]
        product['category'] = "MENS"
        product['description'] = sel.xpath("//meta[@name='description']/@content").extract()
        return product