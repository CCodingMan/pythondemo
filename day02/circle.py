#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    @File: fractal_tree.py    
    @Modify Time: 2019/3/20 20:40
    @Author: 刘佳佳
    @Version: 1.0
    @Description: 输入半径计算圆的周长和面积
"""

import math


def circle_():
    radius = float(input('请输入圆的半径: '))
    perimeter = 2 * math.pi * radius
    area = math.pi * radius * radius
    print('周长: %.2f' % perimeter)
    print('面积: %.2f' % area)


def main():
    circle_()


if __name__ == '__main__':
    main()
