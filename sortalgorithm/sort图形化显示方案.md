# 方案一

https://q.cnblogs.com/q/89924/
使用Canvas划线，效果较为简单。

代码如下：

```python
import time
from tkinter import *

a=[1,9,5,6,8,1]

class CanvasDemo():
    #n1=70
    #n2=n1+40
    d1=390
    d2=d1-60
    weiyi=len(a)-1
    def __init__(self):

        n1=70
        n2=n1+40
        window=Tk()
        window.title("冒泡排序演示")
        self.canvas=Canvas(window,width=500,height=400,bg='white')##设置画布大小，颜色
        self.canvas.pack()
        frame=Frame(window)
        frame.pack()
        ##self.paixu()
        self.displayRect()
        self.n1=n1+60
        self.n2=n2+60
        btString=Button(frame,text="执行",command=self.paixu)
        btString.grid(row=1,column=6)
        window.mainloop()


    def displayRect(self):##打印表格
        self.canvas.create_rectangle(60,30,420,90,tags="rect")##左上右下
        self.canvas.create_rectangle(120,30,360,90,tags="rect")
        self.canvas.create_rectangle(180,30,300,90,tags="rect")
        self.canvas.create_rectangle(240,30,240,90, tags="rect")
    def paixu(self):

        for i in range(0,len(a)):
            j=len(a)-1##添加交换之前
            self.weiyi=len(a)-1
            while j>i:
                self.displayString2()
                time.sleep(1)
                #if j>i:
                 #   self.canvas.delete("int")

                ##self.weiyi=len(a)-1
                self.displayString3()
                time.sleep(1)
                if a[j-1]>a[j]:
                    a[j-1],a[j]=a[j],a[j-1]
                #j=j-1
                self.displayString4()
                if j>=i:
                    self.canvas.delete("int")
                self.displayString1()##打印交换之后的
                time.sleep(1)

                if j>=i:
                    self.canvas.delete("int")
                j=j-1
            self.displayString1()



    def displayLine(self):## 设置箭头指向
        self.canvas.create_line(self.n2,30,self.n2,10,self.n2+60,10,self.n2+60,30,width=1,arrow="last",tags="line")

    def displayString1(self):## 打印序列
        n1=90
        ##time.sleep(1)

        for z in range(len(a)):
            self.canvas.create_text(n1,60,text="%s"%a[z],font="Times 20 bold ",tags="int")
            n1=n1+60
        self.canvas.update()
        #self.update()
        #time.sleep(0.5)

    def displayString2(self):
        n2=90
        for z in range(len(a)):
            if z!=self.weiyi and z!=self.weiyi-1:
                self.canvas.create_text(n2,60,text="%s"%a[z],font="Times 20 bold ",tags="int")
            n2=n2+60
        self.canvas.update()
        self.weiyi=self.weiyi-1
    def displayString3(self):
        n2=90
        for z in range(len(a)):
            if z==self.weiyi:
                if a[z]>a[z+1]:
                    self.canvas.create_line(n2,30,n2,10,n2+60,10,n2+60,30,width=1,arrow="last",tags="line")
                self.canvas.create_text(n2,60,text="%s"%a[z],font="Times 20 bold ",tags="int1")
                self.canvas.create_text(n2+60,60,text="%s"%a[z+1],font="Times 20 bold",tags="int1")
                for x in range(0,10):
                    self.canvas.move("int1",0,20)
                    self.canvas.move("int12",0,20)
                    self.canvas.update()
                    time.sleep(0.1)
                    if(x==9):
                        self.canvas.delete("int1")
            n2=n2+60
        self.canvas.update()
    def displayString4(self):
        n2=90
        for z in range(len(a)):
            if z==self.weiyi:
                self.canvas.create_text(n2,300,text="%s"%a[z],font="Times 20 bold ",tags="int2")
                self.canvas.create_text(n2+60,300,text="%s"%a[z+1],font="Times 20 bold ",tags="int2")
                for x in range(0,10):
                    self.canvas.move("int2",0,-20)
                    self.canvas.update()
                    time.sleep(0.1)
                    if(x==9):
                        self.canvas.delete("int2","line")
            n2=n2+60

CanvasDemo()
```



# 方案二

https://github.com/ZQPei/Sorting_Visualization
使用pygame，动画效果好。

# 方案三

https://blog.csdn.net/u010720408/article/details/96716515
使用matplotlib画。

代码如下：

```python
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 00:32:06 2019
pyplot_dynamic_draw_sample_01.py
在ipython中无法体现出动态效果，需要再window得cmd中启动pyton（linux也是一样console启动），然后输入下面得文件就能看到效果
@author: Sudaxia
"""
# matplotline   #jupyter ipython中别加inline就能画图出来
import matplotlib.pyplot as plt
import random

# plt.ion()
plt.ioff()


def swapAndDraw(data, x1, x2):
    temp1height = tempbar[x1].get_height()
    tempbar[x1].set_height(tempbar[x2].get_height())
    tempbar[x2].set_height(temp1height)
    tempbar[x2].set_fc("red")
    plt.draw()
    plt.pause(0.5)
    tempbar[x2].set_fc("green")  # 记得颜色换回来


# 冒泡排序
data = random.sample(range(20), 20)

print(data)

n = len(data)
tempbar = plt.bar(range(n), data, fc="green")

for m in range(n):  # 趟数
    for i in range(n - m - 1):
        if data[i] > data[i + 1]:
            data[i + 1], data[i] = data[i], data[i + 1]
            swapAndDraw(data, i, i + 1)

print(data)

plt.ioff();
# plt.show();
```

方案四
开始想到可以直接使用animation画柱状图，然后周期根据排序结果改变柱状图的高度作为排序依据。后来发现结合方案三也可以直接设定单个柱的高度。

代码：

```python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import time


# 测试一：一次画出全部柱子，由list改色
plt.figure(figsize=(6, 5))

# 配色
colora=['black','red','red','red']
colorb=['red','black','red','red']
colorc=['red','red','black','red']
colord=['red','red','red','black']

# 开始
for i in range(5):
    plt.clf()
    num_list = [1.5, 0.6, 7.8, 6]

    plt.bar(range(len(num_list)), num_list, alpha=0.5, width=0.3, color=colora, edgecolor='deepskyblue', tick_label=num_list,  lw=3)
    plt.pause(0.3)


    plt.clf()
    num_list = [0.6, 7.8, 6, 1.5]

    plt.bar(range(len(num_list)), num_list, alpha=0.5, width=0.3, color=colorb, edgecolor='deepskyblue', tick_label=num_list,  lw=3)
    plt.pause(0.3)


    plt.clf()
    num_list = [7.8, 6, 1.5, 0.6]

    plt.bar(range(len(num_list)), num_list, alpha=0.5, width=0.3, color=colorc, edgecolor='deepskyblue', tick_label=num_list,  lw=3)
    plt.pause(0.3)


    plt.clf()
    num_list = [6, 1.5, 0.6, 7.8]

    plt.bar(range(len(num_list)), num_list, alpha=0.5, width=0.3, color=colord, edgecolor='deepskyblue', tick_label=num_list,  lw=3)
    plt.pause(0.3)


# 测试二：使用函数调整柱子
plt.clf()
plt.pause(3)

num_list = [1.5, 0.6, 7.8, 6]

sortbar = plt.bar(range(len(num_list)), num_list, alpha=0.5, width=0.3, color='black', edgecolor='deepskyblue', tick_label=num_list, lw=3)

sortbar[0].set_fc("red")

# 开始
for cnt in range(10):
    for i in range(len(num_list)):
        if i < len(num_list)-1:
            sortbar[i].set_fc("black")
            tempheight = sortbar[i].get_height()
            sortbar[i].set_height(sortbar[i+1].get_height())

            sortbar[i+1].set_fc("red")
            sortbar[i+1].set_height(tempheight)

            plt.pause(0.2)
        else:
            break

# 结束
plt.show()
```

最后完成了一个单个冒泡还不错的效果，实现代码如下：

```python
#!/usr/bin/python3
# 文件名: sort.py
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from random import randrange, shuffle


if __name__ == '__main__':

    array = []

    # 范围内随机取12个数值
    while len(array) < 20:
        array.append(randrange(5, 50, 5))

    # 打乱数组
    shuffle(array)

    sortbar = plt.bar(range(len(array)), array, alpha=0.5, width=0.3, color='red', edgecolor='deepskyblue', tick_label=array, lw=3)

    print('排序前数组：{}'.format(array))



    # 遍历所有数组元素
    for i in range(len(array)-1):

        print("from 0 to ", len(array) - i - 1)

        swapped = False

        # last i elements are already in place
        for j in range(len(array) - i - 1):

            sortbar[j].set_fc("deepskyblue")
            sortbar[j + 1].set_fc("deepskyblue")

            if (array[j] > array[j+1]) :
                swapped = True
                array[j], array[j+1] = array[j+1], array[j]

                tempheight = sortbar[j].get_height()
                sortbar[j].set_height(sortbar[j + 1].get_height())

                sortbar[j + 1].set_height(tempheight)

            plt.pause(0.01)

            sortbar[j].set_fc("red")
            sortbar[j+1].set_fc("black")

        if not swapped:
            break

        plt.pause(0.5)

    if swapped:
        sortbar[0].set_fc("black")

    plt.pause(0.1)

    print('排序后数组：{}'.format(array))

    # 结束
    plt.show()
```

