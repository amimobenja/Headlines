from scrapy.item import Item, Field

class HeadlinesItem(Item):
    title = Field()
    description = Field()
    link = Field()
