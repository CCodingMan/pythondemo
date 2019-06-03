#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    @File: fractal_tree.py    
    @Modify Time: 2019/3/20 20:40
    @Author: 刘佳佳
    @Version: 1.0
    @Description: 运算符的使用
"""


def operator_():
    a = 5
    b = 10
    c = 3
    d = 4
    e = 5
    a += b
    a -= c
    a *= d
    a /= e
    print("a = ", a)

    flag1 = 3 > 2
    flag2 = 2 < 1
    flag3 = flag1 and flag2
    flag4 = flag1 or flag2
    flag5 = not flag1
    print("flag1 = ", flag1)
    print("flag2 = ", flag2)
    print("flag3 = ", flag3)
    print("flag4 = ", flag4)
    print("flag5 = ", flag5)
    print(flag1 is True)
    print(flag2 is not False)


def main():
    operator_()


if __name__ == '__main__':
    main()