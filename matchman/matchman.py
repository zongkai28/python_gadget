# pythonh制作抖音上非常火的送心小人
# 参考：https://www.baidu.com/link?url=jOqWhjO5X0nMi5Oj22ThMGx4s2DYeJWIVGPOWpBp75o3Viojd1NGKMfNT3XfQnlapnl5IaPbPSncE9J-Dy2et_qjrsVY4S4xc1nHfnwLeNy&wd=&eqid=dd68a6fe000718a2000000045d985a30

# python 3.7

import turtle

t = turtle.Turtle()

def fd(a):
    t.forward(a)

t.pensize(3)
t.hideturtle()
t.speed(10)

def up():
    t.penup()

def down():
    t.pendown()

t.hideturtle()
t.speed(10)
t.fillcolor('red')
up()
t.goto(-200, 80)
down()
t.pencolor('pink')
t.write('史先生：', font=("Courier", 15, "bold"))

# 小人
up()
t.goto(-100, 0)
down()
t.pencolor('black')
t.pensize(3)
t.circle(20)
t.setheading(270)
fd(50)
t.setheading(225)
fd(35)
t.goto(-100, -50)
t.setheading(0)
fd(35)
t.setheading(270)
fd(28)
up()
t.goto(-100, -15)
down()
t.setheading(0)
fd(30)
t.setheading(45)
fd(12)

up()
t.goto(-100, -25)
down()
t.setheading(0)
fd(40)
t.setheading(-45)
fd(12)

# 小红心
def xin():
    up()
    t.goto(0, 20)
    t.pencolor('red')
    down()
    t.begin_fill()
    t.speed(10)
    t.setheading(135)
    for i in range(10):
        t.left(20)
        fd(3)
    for i in range(6):
        t.left(10)
        fd(3.5)
    t.end_fill()
    up()
    t.goto(0, 20)
    down()
    t.begin_fill()
    t.setheading(45)
    for i in range(10):
        t.right(20)
        fd(3)
    for i in range(6):
        t.right(10)
        fd(3.5)
    t.end_fill()
xin()

# 大红心
def move():
    t.pencolor('red')
    t.speed(10)
    t.setheading(135)
    for i in range(100):
        t.left(2)
        fd(1)
    for i in range(5):
        t.left(1)
        fd(6.83)
    up()
    t.goto(100, 50)
    down()
    t.setheading(45)
    for i in range(100):
        t.right(2)
        fd(1)
    for i in range(5):
        t.right(1)
        fd(6.83)

up()
t.goto(100, 50)
down()
t.begin_fill()
move()

# 大红心填色
t.end_fill()
up()
t.goto(0, -100)
down()
t.pencolor('pink')
t.write('**小可爱**', font=("Courier", 20, "bold"))