#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    @File: fractal_tree.py    
    @Modify Time: 2019/3/20 20:40
    @Author: 刘佳佳
    @Version: 1.0
    @Description: 字符串常用操作
"""


def string_():
    str1 = 'hello, world!'
    print('字符串的长度是:', len(str1))
    print('单词首字母大写: ', str1.title())
    print('字符串变大写: ', str1.upper())
    # str1 = str1.upper()
    print('字符串是不是大写: ', str1.isupper())
    print('字符串是不是以hello开头: ', str1.startswith('hello'))
    print('字符串是不是以hello结尾: ', str1.endswith('hello'))
    str2 = '- \u9a86\u660a'
    str3 = str1.title() + ' ' + str2.lower()
    print(str3)


def main():
    string_()


if __name__ == '__main__':
    main()
