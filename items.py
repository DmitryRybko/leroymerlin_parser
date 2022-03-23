# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Compose


def process_price(price_item):

    price_string = price_item[0].replace(" ", "")
    result = int(price_string)
    return result


class LeroyparserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field(input_processor=Compose(process_price))
    image_urls = scrapy.Field()
    images = scrapy.Field()
    _id = scrapy.Field()
