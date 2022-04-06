# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VrbodataItem(scrapy.Item):
    # define the fields for your item here like:
    # Location, Title, Sleep, Bedroom, Price and Image link

    property_name = scrapy.Field()
    property_price = scrapy.Field()
    property_thumb = scrapy.Field()
    property_details = scrapy.Field()


