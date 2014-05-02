from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from clobot.items import ProductItem

class UniqloSpider(CrawlSpider):
    
    name = "uniqlo"
    allowed_domains = ["uniqlo.com"]
    start_urls = ["http://www.uniqlo.com/us/"]
    rules = (
             Rule(SgmlLinkExtractor(allow=('/us/(wo)?men/.*\d+.html')), callback='parse_product'),
             Rule(SgmlLinkExtractor(allow=('/us/(wo)?men/'), )), 
             )
    
    def parse_product(self, response):
        sel = Selector(response)
        product = ProductItem()
        product['url'] = response.url
        product['name'] = (''.join(sel.xpath("//meta[@property='og:title']/@content").extract())).split('|')[0]
        product['image'] = sel.xpath("//meta[@property='og:image']/@content").extract()
        product['brand'] = "UNIQLO"
        product['category'] = (''.join(response.url.split('/')[4]))+'s'
        product['description'] = ''.join(sel.xpath("//meta[@name='description']/@content").extract())
        return product