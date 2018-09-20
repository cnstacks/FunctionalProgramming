#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FunctionalProgramming 
# Software: PyCharm
# Time    : 2018-09-20 12:25
# File    : 5.文件处理-智能检测编码的工具.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
""
"""
1、chardet模块
2、安装:pip3 install chardet;
3、安装第三方工具包的方法：pip3 install 模块名
4、Useage:import chardet;
"""
import chardet

f = open(file="兼职白领学生空姐模特护士联系方式.txt.bak", mode="rb")
data = f.read()
print(data)

print(chardet.detect(data))  # {'encoding': 'GB2312', 'confidence': 0.99, 'language': 'Chinese'}
print(data.decode("gb2312"))  # decode解码;
