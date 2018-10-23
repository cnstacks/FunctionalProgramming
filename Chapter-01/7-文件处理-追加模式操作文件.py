#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FunctionalProgramming 
# Software: PyCharm
# Time    : 2018-09-20 20:55
# File    : 7-文件处理-追加模式操作文件.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org


f = open(file="兼职白领学生空姐模特护士联系方式.txt.bak", mode="ab")
f.write("\n崔晓昭 石家庄 183 115 13811221893".encode("GBK"))
f.close()
