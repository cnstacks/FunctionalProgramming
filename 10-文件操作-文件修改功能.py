#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FunctionalProgramming 
# Software: PyCharm
# Time    : 2018-09-20 21:24
# File    : 10-文件操作-文件修改功能.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
""
"""
文件修改功能；
硬盘的存储原理决定了，数据只能整体移动；
word or vim的工作原理是边读边写！先加载至内存中，然后再修改，重新写入硬盘，覆盖写！
"""
import os

f_name = "兼职白领学生空姐模特护士联系方式.txt"
f_new_name = "%s.new" % f_name

old_str = "崔晓昭"
new_str = "cuixiaozhao"
f = open(file=f_name, mode="r", encoding="GBK")
f_new = open(file=f_new_name, mode="w", encoding="GBK")

for line in f:
    if old_str in line:
        line = line.replace(old_str, new_str)
    f_new.write(line)

f.close()
f_new.close()

os.rename(f_new_name,f_name)