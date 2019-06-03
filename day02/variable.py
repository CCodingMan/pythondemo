#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    @File: fractal_tree.py    
    @Modify Time: 2019/3/20 20:40
    @Author: 刘佳佳
    @Version: 1.0
    @Description: 
"""


# 使用变量保存数据并进行操作
def variable1():
    a = 100
    b = 3
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    # a/b后获取整数部分
    print(a // b)
    # 取余
    print(a % b)
    # b个a相乘
    print(a ** b)


# 将input函数输入的数据保存在变量中并进行操作
def variable2():
    a = int(input('a = '))
    b = int(input('b = '))
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    # a/b后获取整数部分
    print(a // b)
    # 取余
    print(a % b)
    # b个a相乘
    print(a ** b)


# 格式化输出
def variable3():
    a = int(input('a = '))
    b = int(input('b = '))
    print('%d + %d = %d' % (a, b, a + b))
    print('%d - %d = %d' % (a, b, a - b))
    print('%d * %d = %d' % (a, b, a * b))
    print('%d / %d = %f' % (a, b, a / b))
    print('%d // %d = %d' % (a, b, a // b))
    # 注意%需转义
    print('%d %% %d = %d' % (a, b, a % b))
    print('%d ** %d = %d' % (a, b, a ** b))


# 检查变量的类型
def variable4():
    a = 100
    b = 1000000000000000000
    c = 12.345
    d = 1 + 5j
    e = 'A'
    f = 'hello, world'
    # 注意：python中的布尔类型True,False首字母大写
    g = True
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))
    print(type(f))
    print(type(g))


# 类型转换
def variable5():
    a = 100
    b = str(a)
    c = 12.345
    d = str(c)
    e = '123'
    f = int(e)
    g = '123.456'
    h = float(g)
    i = False
    j = str(i)
    k = 'hello'
    m = bool(k)
    # 将整数转换成该编码对应的字符串（一个字符）
    n = chr(a)
    # 将字符串（一个字符）转换成对应的编码（整数）
    p = ord(n)

    print(a)
    print(type(a))
    print(b)
    print(type(b))
    print(c)
    print(type(c))
    print(d)
    print(type(d))
    print(e)
    print(type(e))
    print(f)
    print(type(f))
    print(g)
    print(type(g))
    print(h)
    print(type(h))
    print(i)
    print(type(i))
    print(j)
    print(type(j))
    print(k)
    print(type(k))
    print(m)
    print(type(m))
    print(n)
    print(type(n))
    print(p)
    print(type(p))


def main():
    # variable1()
    # variable2()
    # variable3()
    # variable4()
    variable5()


if __name__ == '__main__':
    main()
