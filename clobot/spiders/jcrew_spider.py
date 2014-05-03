from scrapy.contrib.spiders import SitemapSpider
from scrapy.selector import Selector

from clobot.items import ProductItem

class JCrewSpider(SitemapSpider):
    name = "jcrew"
    sitemap_urls = ["https://www.jcrew.com/robots.txt"]
    sitemap_rules = [
                     ('/(wo)?mens_category/.*/PRDOVR~.+/.+\.jsp', 'parse_product'),
             ]
    
    def parse_product(self, response):
        sel = Selector(response)
        product = ProductItem()
        product['url'] = response.url
        product['name'] = ''.join(sel.xpath("//meta[@property='og:title']/@content").extract())
        product['image'] = sel.xpath("//meta[@property='og:image']/@content").extract()
        product['brand'] = "J.CREW"
        product['category'] = (response.url.split('/')[3]).split('_')[0]
        product['description'] = ''.join(sel.xpath("//meta[@name='description']/@content").extract())
        #setting color to empty string because page returned by jcrew to crawlers does not contain  product color information
        product['color'] = ''
        return product