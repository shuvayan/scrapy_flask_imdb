# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item
from scrapy.item import Field


class ImdbItem(scrapy.Item):
    # define the fields for your item here like:
    movie_id = Field()
    img_src = Field()
    name = Field()
    produced = Field()
    duration = Field()
    genre = Field()
    released = Field()
    rating = Field()
    rating_cnt = Field()
    description = Field()
    director = Field()
    writer = Field()
    cast = Field()
    
