from scrapy.item import Item, Field

class ProductItem(Item):
    url = Field()
    name = Field()
    image = Field()
    brand = Field()
    category = Field()
    description = Field()
    color = Field()