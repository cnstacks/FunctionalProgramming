#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FunctionalProgramming 
# Software: PyCharm
# Time    : 2018-09-20 21:01
# File    : 8-文件处理-混合模式操作文件.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
""

"""
r：
w：
a:
r+:
w+:
rb:
"""
f = open(file="兼职白领学生空姐模特护士联系方式.txt.bak", mode="r+", encoding="GBK")
data = f.read()

print("Content",data)

f.write("\nNewLine 1 崔晓昭")
f.write("\nNewLine 2 崔晓昭")
f.write("\nNewLine 3 崔晓昭")
f.write("\nNewLine 4 崔晓昭")
f.write("\nNewLine 5 崔晓昭")

print("NewContent", f.read())
