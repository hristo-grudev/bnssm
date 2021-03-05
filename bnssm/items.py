import scrapy


class BnssmItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
