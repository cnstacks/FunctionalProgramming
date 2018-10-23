#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FunctionalProgramming 
# Software: PyCharm
# Time    : 2018-09-20 21:08
# File    : 9-文件操作-文件操作的其他功能.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
""
"""
f.read()#字符;
f.seek()#字节；
f.tell()#字节；
f.fileno()
f.flush()
f.readable()
f.readline()
f.seekable()
f.truncate()
f.writeable()
"""
f = open("f_flush_test.txt", "w")
f.write("\ncuixiaozhao")
f.close()
