#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/3 16:23
# @Author  : fengye
# @Site    :
# @File    : Demo01.py
# @Software: PyCharm

import re

pattern = re.compile(r"hello")
match1 = pattern.match("hello,world")
match2 = pattern.match("helloo,world")
match3 = pattern.match("helllo,world")
match4 = pattern.search("hello,world122")

if match1 :
    print match1.group()
else :
    print "match1 匹配失败"

if match2:
    print  match2.group()
else:
    print "match2 匹配失败"

if match3 :
    print match3.group()
else :
    print  "match3 匹配失败"


if match4:
    print match4.group(0)
    print  match4.span()
else :
    print "match 4 匹配失败"