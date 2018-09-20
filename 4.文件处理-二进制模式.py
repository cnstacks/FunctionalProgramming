#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FunctionalProgramming 
# Software: PyCharm
# Time    : 2018-09-20 12:21
# File    : 4.文件处理-二进制模式.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
""
"""
1、二进制模式打开文件，用于远程传输，给计算机读取；
"""
#f = open(file="兼职白领学生空姐模特护士联系方式.txt.bak",mode="rb",encoding="GBK")#ValueError: binary mode doesn't take an encoding argument
f = open(file="兼职白领学生空姐模特护士联系方式.txt.bak",mode="rb")
data = f.read()
print(data)#
"""
b'\xd0\xd5\xc3\xfb\t    \xb5\xd8\xc7\xf8\t\xc9\xed\xb8\xdf\t\xcc\xe5\xd6\xd8\t\xb5\xe7\xbb\xb0\n\xbf\xf6\xd3\xbd\xc3\xdb \t\xb1\xb1\xbe\xa9\t171\t48\t13651054608\n\xcd\xf5\xd0\xc4\xd1\xd5 \t\xc9\xcf\xba\xa3\t169\t46\t13813234424\n\xc2\xed\xcf\xcb\xd3\xf0 \t\xc9\xee\xdb\xda\t173\t50\t13744234523\n\xc7\xc7\xd2\xe0\xb7\xc6 \t\xb9\xe3\xd6\xdd\t172\t52\t15823423525\n\xc2\xde\xc3\xce\xd6\xf1 \t\xb1\xb1\xbe\xa9\t175\t49\t18623423421\n\xc1\xf5\xc5\xb5\xba\xad \t\xb1\xb1\xbe\xa9\t170\t48\t18623423765\n\xd4\xc0\xc4\xdd\xc4\xdd \t\xc9\xee\xdb\xda\t177\t54\t18835324553\n\xba\xd8\xcd\xf1\xdd\xe6 \t\xc9\xee\xdb\xda\t174\t52\t18933434452\n\xd2\xb6\xe8\xf7\xdd\xe6\t\xc9\xcf\xba\xa3\t171\t49\t18042432324\n\xb6\xc5\xe6\xa9\xe6\xa9 \xb1\xb1\xbe\xa9  167 49 13324523342'
"""
f.close()

