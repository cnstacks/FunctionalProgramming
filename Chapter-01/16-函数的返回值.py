#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: FunctionalProgramming 
# Software: PyCharm2018.3
# DateTime: 2018-10-23 13:08
# File: 16-函数的返回值.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org


def stu_register(name, age, position="PY", country="CN"):
    print("注册学生信息".center(50, "-"))
    print("姓名:", name)
    print("年龄:", age)
    print("国籍:", country)
    print("岗位:", position)

    if age > 22:
        return False
    else:
        return True


regist_status = stu_register("崔晓昭", 20, position="Python开发工程师", country="中国")
if regist_status:
    print("注册成功")
else:
    print("你已不再年少，肯定是社会人了，不是学生党啦！")
"""
小结:
1、函数是有返回值的，如果不使用return指定返回值，默认返回None;
2、return代表函数的终止，无论后面有多少代码，都不会执行；
3、return只能返回一个值，如果想返回多个，程序会自动打包成元组;
即return表示函数的结束！
"""