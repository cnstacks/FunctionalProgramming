#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FunctionalProgramming 
# Software: PyCharm
# Time    : 2018-09-20 12:31
# File    : 6-1-文件处理-写模式操作文件.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

""
""" 
1、边读边处理方式处理文件；
2、默认有一个换行符\n，循环时候自动添加一个空行，so 为2个；
3、w模式永远是清空操作，如果文件存在，先清空再写入，一定要慎用！
"""
# f = open("兼职白领学生空姐模特护士联系方式1.txt", "wb")
# f.write("崔晓昭".encode("gbk"))
# f.close()


f = open("兼职白领学生空姐模特护士联系方式1.txt", "wb")
f.write("cuixiaozhao".encode("gbk"))
f.close()
