from scrapy.exceptions import DropItem
from w3lib.html import remove_comments, remove_tags, remove_entities

class InvalidItemPipeline(object):
    """A pipeline for filtering out items that 
    do not contain the minimum required data.
    """
    
    def process_item(self, item, spider):
        if not item['name']:
            raise DropItem("Missing item name in %s" %item)
        elif not item['category']:
            raise DropItem("Missing item category in %s" %item)
        elif not item['brand']:
            raise DropItem("Missing item brand in %s" %item)
        else:
            return item
        
class ProductItemPipeline(object):
    """A pipeline for sanitizing items by removing the html 
    in the description and various other vanity changes.
    """
    
    def process_item(self, item, spider):
        item['brand'] = item['brand'].upper()
        item['category'] = item['category'].upper()
        item['name'] = ''.join(item['name']).encode('ascii', 'ignore')
        item['description'] = ProductItemPipeline.cleanHtml(''.join(item['description']))
        return item

    @staticmethod
    def cleanHtml(html):
        return remove_comments(remove_tags(remove_entities(html))).encode('ascii','ignore')