# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PycloudItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class DingdianItem(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()
    novelurl = scrapy.Field()
    serialstatus = scrapy.Field()
    category = scrapy.Field()
    name_id = scrapy.Field()

class DcontentItem(scrapy.Item):
    id_name = scrapy.Field()
    chaptercontent = scrapy.Field()
    num = scrapy.Field()
    chapterurl = scrapy.Field()
    chaptername = scrapy.Field()


class HaoduofuliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    category = scrapy.Field()  # 类型
    title = scrapy.Field()  # 标题
    imgurl = scrapy.Field()  # 图片的地址
    yunlink = scrapy.Field()  # 百度云盘的连接
    password = scrapy.Field()  # 百度云盘的密码
    url = scrapy.Field()  # 页面的地址

class MzituScrapyItem(scrapy.Item):
    name = scrapy.Field()
    image_urls = scrapy.Field()
    url = scrapy.Field()
    pass

