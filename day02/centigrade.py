#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    @File: fractal_tree.py    
    @Modify Time: 2019/3/20 20:40
    @Author: 刘佳佳
    @Version: 1.0
    @Description: 将华氏温度转换为摄氏温度 F = 1.8C + 32
"""


def centigrade_():
    f = float(input('请输入华氏温度: '))
    c = (f - 32) / 1.8
    print('%.1f华氏度 = %.1f摄氏度' % (f, c))


def main():
    centigrade_()


if __name__ == '__main__':
    main()
