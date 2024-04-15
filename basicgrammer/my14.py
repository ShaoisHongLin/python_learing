# 如何用turtle画出坐标点,并连线。
import turtle
import math
# 先用变量定义出坐标点。
x1,y1 = 100,100  # 第一象限
x2,y2 = 100,-100  # 第二象限
x3,y3 = -100,-100  # 第三象限
x4,y4 = -100,100  # 第四象限

# turtle.goto就是控制你的画笔的坐标，前往...
# turtle.penup()抬起笔
# turtle.pendown()放下笔
turtle.penup()
turtle.goto(x1, y1)  # 移动画笔由0.0到x1,y1
turtle.pendown()
turtle.goto(x2, y2)  # 继续移动

turtle.goto(x3, y3)
turtle.goto(x4, y4)

#turtle.done() # 不直接关闭，而是等待一下。


# 可以导入math之后，用sqrt的开根号，用'两点间距离公式'求出值，并存在一个变量里。
# turtle.write() 可以在此时画笔位置标注出对应的值。

distance=math.sqrt((x1-x2)**2+(y1-y2)**2)
turtle.write(distance)

turtle.done()