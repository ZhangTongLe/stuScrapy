#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/9 14:15
# @Author  : fengye
# @Site    : 
# @File    : WebSpider.py
# @Software: PyCharm

import scrapy

class WebSpider(scrapy.Spider):
    name = 'quotes'
    #设置 start_urls 属性，替代实现 start_requests()
    start_urls = [
         'http://quotes.toscrape.com/page/1/',
         'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'text': quote.xpath('span[@class="text"]/text()').extract_first(),
                'author': quote.xpath('span/small[@class="author"]/text()').extract_first(),
                'tags': quote.xpath('div/a[@class="tag"]/text()').extract(),
            }