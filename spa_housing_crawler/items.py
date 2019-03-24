# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class House(scrapy.Item):

    # Metadata
    ad_last_update = scrapy.Field()
    obtention_date = scrapy.Field()

    # ID
    house_id = scrapy.Field()

    # Location Features
    loc_street = scrapy.Field()
    loc_city = scrapy.Field()
    loc_zone = scrapy.Field()

    # Price
    price = scrapy.Field()

    # House Properties
    lift = scrapy.Field()
    bath_num = scrapy.Field()
    construct_date = scrapy.Field()
    orientation = scrapy.Field()
    energetic_certif = scrapy.Field()
    floor = scrapy.Field()
    room_num = scrapy.Field()
    m2_real = scrapy.Field()
    m2_useful = scrapy.Field()
    condition = scrapy.Field() # Second Hand / Well Conserved ...
    house_type = scrapy.Field()
    heating = scrapy.Field()
    ground_size = scrapy.Field()
    kitchen = scrapy.Field()
    garage = scrapy.Field()
    unfurnished = scrapy.Field()

    # Extra House Equipment ------>  (Yes = 1 , No = 0)
    storage_room = scrapy.Field()       # trastero
    built_in_wardrobe = scrapy.Field()  # Armario empotrado
    terrace = scrapy.Field()
    balcony = scrapy.Field()
    garden = scrapy.Field()
    chimney = scrapy.Field()
    air_conditioner = scrapy.Field()
    reduced_mobility = scrapy.Field()
    swimming_pool = scrapy.Field()

    # Ad Description
    ad_description = scrapy.Field()