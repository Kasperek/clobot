
class ProductItemPipeline(object):
    
    def process_item(self, item, spider):
        item['brand'] = item['brand'].upper()
        item['category'] = item['category'].upper()
        return item
