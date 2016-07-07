# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirbnbchicagoItem(scrapy.Item):
    # define the fields for your item here like:
    room_description = scrapy.Field()
    host_name = scrapy.Field()
    price_room = scrapy.Field()
    latitud = scrapy.Field()
    longitud = scrapy.Field()
    pass
