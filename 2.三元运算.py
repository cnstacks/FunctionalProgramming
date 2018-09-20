#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: FunctionalProgramming 
# Software: PyCharm
# Time    : 2018-09-20 12:00
# File    : 2.三元运算.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

""
"""
作用：对简单条件的简写，节省代码量;
"""
# No.01
name = 'cuixiaozhao'
if name is 'cuixiaozhao':
    ceo = True
    print("ceo:", ceo)
else:
    ceo = False
    print("ceo:", ceo)

# No.02
s = ceo = True if 'cuixiaozhao' else False
print("s:", s)

# No.03
a = 1993
b = 1995
val = a if a < b else b
print("val", val)
