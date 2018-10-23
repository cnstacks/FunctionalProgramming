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
