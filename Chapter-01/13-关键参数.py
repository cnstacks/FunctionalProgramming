#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: FunctionalProgramming 
# Software: PyCharm2018.3
# DateTime: 2018-10-23 11:33
# File: 13-关键参数.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org
""
"""
概念梳理：
1、位置参数；
2、默认参数；
3、关键参数；
"""


def stu_register(name, age, course="Py", country="CN"):
    print("学生注册信息:")
    print(name, age, course, country)


stu_register("cxz", 26, course="计算机科学与技术", country="中国")
stu_register("李亚辉", course="MBA", age=28)
stu_register("石少普", 28, country="美国", course="文学")
stu_register(26, "宋少璇", country="USA", course="商务礼仪", )
