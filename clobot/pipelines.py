from scrapy.exceptions import DropItem
from w3lib.html import remove_comments, remove_tags, remove_entities

class InvalidPipeline(object):
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
        elif not item['description']:
            raise DropItem("Missing item description in %s" %item)
        else:
            return item
        
class SanitizationPipeline(object):
    """A pipeline for sanitizing items by removing html and converting 
    encoding to ascii as well as other various other vanity changes.
    """
    
    def process_item(self, item, spider):
        item['brand'] = item['brand'].upper()
        item['category'] = item['category'].upper()
        item['name'] = SanitizationPipeline.clean(item['name'])
        item['description'] = SanitizationPipeline.clean(item['description'])
        item['color'] = SanitizationPipeline.clean(item['color']).upper()
        return item

    @staticmethod
    def clean(s):
        return SanitizationPipeline.cleanHtml(s).strip()
        
    @staticmethod
    def cleanHtml(html):
        return remove_comments(remove_tags(remove_entities(html))).encode('ascii','ignore')
    

