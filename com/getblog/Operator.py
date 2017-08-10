#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/3 16:23
# @Author  : Aries
# @Site    : 
# @File    : Operator.py
# @Software: PyCharm

import WebSpider

spider = WebSpider.WhySpider()

#print spider.send_get('http://172.24.10.200/module/member/orderDetail.ac?id=51')

print spider.send_get("http://www.baidu.com")

spider.set_mobile()
print spider.send_get("http://www.baidu.com")
