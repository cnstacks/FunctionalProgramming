#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: FunctionalProgramming 
# Software: PyCharm2018.3
# DateTime: 2018-10-23 12:59
# File: 15-非固定参数2.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org

def func(name, *args, **kwargs):
    print(name, args, kwargs)


func("崔晓昭", 26, "特斯拉的男人", "年薪500W", "终身财富10000亿美金", addr="河北省石家庄市",
     tel=13811221893)  # 崔晓昭 (26, '特斯拉的男人', '年薪500W', '终身财富10000亿美金') {'addr': '河北省石家庄市', 'tel': 13811221893}

info = {
    'degree': '清华大学',
    'desc': '晓昭慈善基金创始人',
    'high': '184CM',
}
func('cuixiaozhao', **info)  # cuixiaozhao () {'degree': '清华大学', 'desc': '晓昭慈善基金创始人', 'high': '184CM'}

"""
小结:
1、Python的非固定参数，在函数定义时候指定;
2、*args传入值的类型为元组
3、**kwargs传入值的类型为字典
4、调用函数的时候，可以直接写成元组或者字典，或者使用*或者**加上变量名进行传值；
"""