#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/8 11:22
# @Author  : fengye
# @Site    : 
# @File    : QSBK.py
# @Software: PyCharm

import  urllib2 ,re,thread,time

class QSBK :

    def __init__(self):
        self.page = 1
        self.enable = False
        self.pages = []

    def GetPage(self,page):
        myUrl = "https://www.qiushibaike.com/hot/page/" + page + "/"
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        request = urllib2.Request(myUrl,headers=headers)
        responsePage = urllib2.urlopen(request).read().decode("utf-8")

        pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div.*?' +
                             'content">(.*?)</div>(.*?).*?<div class="stats.*?class="number">(.*?)</i>', re.S)

        pageItems = re.findall(pattern, responsePage)

        pageStories = []

        for pageItem in pageItems:
            hasImg = re.search('img', pageItem[2])
            if not hasImg:
                pageStories.append([pageItem[0].strip(), pageItem[1].strip(), pageItem[3].strip()])

        return pageStories

    # 用于加载新的段子
    def LoadPage(self):
        # 如果用户未输入quit则一直运行
        while self.enable:
            # 如果pages数组中的内容小于2个
            if len(self.pages) < 2:
                try:
                    # 获取新的页面中的段子们
                    myPage = self.GetPage(str(self.page))
                    self.page += 1
                    self.pages.append(myPage)
                except:
                    print '无法链接糗事百科！'
            else:

                time.sleep(1)

    def ShowPage(self, nowPage, page):
        for items in nowPage:
            print u'第%d页' % page,items[0].strip(), items[1].strip()
            myInput = raw_input()
            if myInput == "quit":
                self.enable = False
                break

    def Start(self):
        self.enable = True
        page = self.page

        print u'正在加载中请稍候......'

        # 新建一个线程在后台加载段子并存储
        thread.start_new_thread(self.LoadPage, ())

        # ----------- 加载处理糗事百科 -----------
        while self.enable:
            # 如果self的page数组中存有元素
            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage, page)
                page += 1


# ----------- 程序的入口处 -----------
print u"""
---------------------------------------
   程序：糗百爬虫
   版本：0.3
   作者：fengye
   日期：2017-08-08
   语言：Python 2.7
   操作：输入quit退出阅读糗事百科
   功能：按下回车依次浏览今日的糗百热点
---------------------------------------
"""

print u'请按下回车浏览今日的糗百内容：'
raw_input(' ')
myModel = QSBK()
myModel.Start()