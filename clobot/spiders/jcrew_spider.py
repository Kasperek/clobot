from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from clobot.items import ProductItem

class JCrewSpider(CrawlSpider):
    
    name = "jcrew"
    allowed_domains = ["jcrew.com"]
    start_urls = ["https://www.jcrew.com/mens-clothing.jsp"]
    rules = (
             
             Rule(SgmlLinkExtractor(allow=('mens_category'), deny=('PRDOVR',))), 
             #Targets product pages using regex expression matching on urls containing PRDOVR and then calls parse_product to process the page
             Rule(SgmlLinkExtractor(allow=('PRDOVR')), callback='parse_product'),
             
             )
    
    
    
    def parse_product(self, response):
        sel = Selector(response)
        product = ProductItem()
        product['url'] = response.url
        product['name'] = sel.xpath("//meta[@property='og:title']/@content").extract()
        product['image'] = sel.xpath("//meta[@property='og:image']/@content").extract()
        product['brand'] = "JCrew"
        product['category'] = response.url.split('/')[3]
        product['description'] = sel.xpath("//meta[@name='description']/@content").extract()
        
        return product