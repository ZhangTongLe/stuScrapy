#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/3 16:03
# @Author  : Aries
# @Site    : 
# @File    : WebSpider.py
# @Software: PyCharm

import cookielib
import urllib
import urllib2
import re
import string

class WhySpider :

    #初始化爬虫
    def __init__(self):
        self.cookie_jar = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie_jar))
        self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0'}

    #发送get请求
    def send_get(self, get_url):
        result = ''
        try:
            my_request = urllib2.Request(url=get_url,headers=self.header)
            result = self.opener.open(my_request).read()
        except Exception, e:
            print 'Exception:',e
        return result
    #发送Post请求
    def send_post(self, post_url ,post_data):
        result = ''
        try:
            my_request = urllib2.Request(url=post_url , data=post_data ,headers= self.header)
            result = self.opener.open(my_request).read()
        except Exception,e:
            print 'Exception : ',e
        return result

    #模拟电脑
    def set_computer(self):
        user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0'
        self.headers = {'User-Agent': user_agent}

    #模拟手机
    def set_mobile(self):
        user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25'
        self.headers = {'User-Agent': user_agent}