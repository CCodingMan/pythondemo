#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    @File: fractal_tree.py    
    @Modify Time: 2019/3/20 20:40
    @Author: 刘佳佳
    @Version: 1.0
    @Description: 输入年份 如果是闰年输出True 否则输出False
"""


def leap_():
    year = int(input('请输入年份：'))
    result = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
    print(result)


def main():
    leap_()


if __name__ == '__main__':
    main()
