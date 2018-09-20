#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FunctionalProgramming 
# Software: PyCharm
# Time    : 2018-09-20 12:09
# File    : 3.文件操作.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

# Req:如何查看文件内容；
""
"""
1、使用自带记事本、Doc or安装文本编辑器软件，如Notepad++；
2、选中右键，利用文本编辑器软件打开这个file对象；
3、查看文件内容 or 写入或修改文件内容；
4、保存并关闭文件对象，Python中一切皆对象！


文件的操作分为：读、写、修改等操作；
"""
f = open(file='兼职白领学生空姐模特护士联系方式.txt.bak', mode="r", encoding='GBK')
data = f.read()
print(data)
f.close()
