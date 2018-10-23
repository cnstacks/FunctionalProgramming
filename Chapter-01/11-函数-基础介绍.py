#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: FunctionalProgramming 
# Software: PyCharm
# DateTime: 2018-10-23 10:46
# File: 11-函数-基础介绍.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org
""
"""
书籍推荐:《金瓶梅》；
"""
"""
1、函数是什么？f(x) = y
2、计算机中的函数是什么？
3、在不同的编程语言中叫做什么？method or function;
4、如何定义，如何使用？def 关键字定义函数
5、如何调用？函数名+（）
6、如何传入参数？
"""


# No.01-在Python中定义一个函数，打印Hello World！
def sayhi():  # 函数名小写，不传入参数;
    print("进入计算机的世界:Hello World！")


print(sayhi)  # <function sayhi at 0x1089c56a8>
sayhi()  # 函数名 + 括号，进行函数的调用！

# No.02-计算两数之和；
m, n = 9, 11

calc = m + n
print("m与n的和为:", calc)


# No.03-使用函数进行calc;
def calc(m, n):  # 传入参数的写法;
    res = m ** n
    print("打印两个数的乘方", res)


calc(2, 10)

"""
小结:
使用函数进行编程的特性
1、减少重复的代码；
2、使得程序易于扩展；
3、使得程序变得易于维护，修改不同的参数，实现更多的功能！
PS:函数名小写，可传入或不传入参数；
"""
