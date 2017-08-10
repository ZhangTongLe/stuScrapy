# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class QsbkItem(scrapy.Item):
    author = scrapy.Field() #作者
    author_logo = scrapy.Field() #作者头像
    content = scrapy.Field() #内容
    thumb = scrapy.Field() # 图片
    votes = scrapy.Field() # 赞
    comments = scrapy.Field() #评论数