#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    @File: fractal_tree.py    
    @Modify Time: 2019/3/20 20:40
    @Author: 刘佳佳
    @Version: 1.0
    @Description: 通过turtle绘制佩奇
"""
from turtle import *


# 画鼻子
def nose(x, y):
    # 提起海龟
    penup()
    # 将海龟移到指定位置
    goto(x, y)
    # 放下海龟
    pendown()
    # 设置海龟的方向（0-东、90-北、180-西、270-南）
    setheading(-30)
    begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            # 向左转3度
            left(3)
            # 向前走
            forward(a)
        else:
            a = a - 0.08
            left(3)
            forward(a)
    end_fill()
    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    # 设置画笔的颜色(红, 绿, 蓝)
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()
    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()


# 画头
def head(x, y):
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300, -30)
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    setheading(161)
    circle(-300, 15)
    penup()
    goto(-100, 100)
    pendown()
    setheading(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            # 向左转3度
            lt(3)
            # 向前走a的步长
            fd(a)
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()


# 画耳朵
def ears(x, y):
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()
    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 56)
    end_fill()


# 画眼睛
def eyes():
    color((255, 155, 192), "white")
    penup()
    setheading(90)
    forward(-20)
    setheading(0)
    forward(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()
    color((255, 155, 192), "white")
    penup()
    seth(90)
    forward(-25)
    seth(0)
    forward(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()


# 画脸颊
def cheek(x, y):
    color((255, 155, 192))
    penup()
    goto(x, y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()


# 画嘴巴
def mouth(x, y):
    color(239, 69, 19)
    penup()
    goto(x, y)
    pendown()
    setheading(-80)
    circle(30, 40)
    circle(40, 80)


# 设置参数
def setting():
    pensize(4)
    # 隐藏海龟
    hideturtle()
    colormode(255)
    color((255, 155, 192), "pink")
    setup(840, 500)
    speed(10)


# 主函数
def main():
    setting()
    nose(-100, 100)
    head(-69, 167)
    ears(0, 160)
    eyes()
    cheek(80, 10)
    mouth(-20, 30)
    done()


if __name__ == '__main__':
    main()
