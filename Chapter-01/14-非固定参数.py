#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: FunctionalProgramming 
# Software: PyCharm2018.3
# DateTime: 2018-10-23 11:45
# File: 14-非固定参数.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org

""
"""
不想传入固定参数怎么办？
"""


def send_alert(msg, *users):
    for user in users:
        print("发送报警给", user)


# 方式一:
send_alert("CPU使用率居高不下啦！", 'cxz', 'cxs', 'lyh', 'ssp')
print("".center(50, "*"))
send_alert("MEM使用率居高不下啦！", 'cxz')
print("".center(50, "*"))
send_alert("Inode使用率居高不下啦！", 'cxs', 'lyh', 'ssp')
print("".center(50, "*"))
send_alert("Block使用率居高不下啦！", 'lyh', 'ssp')

# 方式二:
print("".center(50, "*"))
send_alert("真的吗？", ['崔晓昭', '李亚辉', '石少普', '宋少璇'])  # 发送报警给 ['崔晓昭', '李亚辉', '石少普', '宋少璇']
send_alert("真的吗？", *['崔晓昭', '李亚辉', '石少普', '宋少璇'])
"""
发送报警给 崔晓昭
发送报警给 李亚辉
发送报警给 石少普
发送报警给 宋少璇
"""
"""
小结:
1、如果传递的参数中出现*user,*args(推荐使用),传递的参数就可以不再是固定个数，传过来的所有参数打包成元组格式;
2、函数名+（）调用的时候，也可以使用*打包传递参数的个数；
3、send_alert("Block使用率居高不下啦！", 'lyh', 'ssp',age=28)，此处的参数位置可以是关键参数的写法；
"""
