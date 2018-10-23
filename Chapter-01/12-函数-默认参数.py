#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: FunctionalProgramming 
# Software: PyCharm2018.3
# DateTime: 2018-10-23 11:14
# File: 12-函数-默认参数.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org


def calc(x, y):  # 形参；
    """
    计算两个数的乘方
    :param x:
    :param y:
    :return:
    """
    res = x ** y
    return res


c = calc(2, 10)  # 实参；
print("计算两个数的乘方:", c)


# 写一个学生注册的函数;
def stu_register(name, age, country, course):
    print("学生注册信息详情:")
    print(name, age, country, course)


stu_register("cuixiaozhao", 26, "China", "Python")
stu_register("liyahui", 27, "USA", "Linux")
stu_register("shishaopu", 28, "UK", "FullStack")
stu_register("liushaoxuan", 29, "Japan", "Java")
stu_register("songshaoxuan", 24, "France", "Ruby")
stu_register("lihaoqian", 23, "Australia", "Shell")
print("".center(50, "*"))


# 默认参数；
def user_register(name, age, course, country="China"):  # country是默认参数；
    print("用户注册信息详情:")
    print(name, age, course, country)


user_register("崔晓昭", 26, "Python", "China")
user_register("李亚辉", 25, "Linux")
user_register("cxz", 25, "Linux", "")  # 注意此处传入的值为空字符，不是None;
user_register("石少普", 24, "Java", "日本")
user_register("宋少璇", 23, "PHP", "英国")
"""
小结：
1、默认参数必须放到位置参数之后；
"""
