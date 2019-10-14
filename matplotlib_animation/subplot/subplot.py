# -*-coding:utf-8-*-
# https://blog.csdn.net/qq_36982160/article/details/80682460
import random
from matplotlib.backends.backend_agg import FigureCanvas
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import seaborn as sns
from matplotlib.image import imread

gesture_i = [0] * 2200
gesture_q = [0] * 2200
acc_first = [0] * 6
acc_second = [0] * 6

acc_first_max_index = 0
acc_second_max_index = 0
acc_first_max = 0
acc_second_max = 0

cur_data_count = 0

update_first_flag = False
update_second_flag = False
name_list = ["Static", "Approach", "Apart", "Click", "Flip", "Circle"]

# 创建画布，包含4个子图
fig = plt.figure(figsize=(15, 10))

bgimg=imread("subplot.jpg")#设置背景图片
fig.figimage(bgimg,resize=True)#设置窗口自适应（背景图片）



ax1 = fig.add_subplot(2, 2, 1)
ax1.set_facecolor('none')#设置该子图背景透明，其他子图同理


ax2 = fig.add_subplot(2, 2, 3)
ax2.set_facecolor('none')



ax3 = fig.add_subplot(2, 2, 2)
ax3.set_facecolor('none')

ax4 = fig.add_subplot(2, 2, 4)
ax4.set_facecolor('none')

# 绘制初始图形
bar1 = ax3.bar(range(len(acc_first)), acc_first, color='rgb', tick_label=name_list)


bar2 = ax4.bar(range(len(acc_first)), acc_first, color='rgb', tick_label=name_list)


x = np.arange(0, 2200, 1)  # x轴

ax1.set_ylim(-1, 1)#设置y轴范围为-1到1
line1, = ax1.plot(x, gesture_i,color='coral')

ax2.set_ylim(-1, 1)
line2, = ax2.plot(x, gesture_q,color='coral')

#初始化函数
def init():
    # 构造开始帧函数init
    # 改变y轴数据，x轴不需要改
    line1.set_ydata(gesture_i)
    line2.set_ydata(gesture_q)
    bar1 = ax3.bar(range(len(acc_first)), acc_first, color='rgb', tick_label=name_list)
    bar2 = ax4.bar(range(len(acc_second)), acc_second, color='rgb', tick_label=name_list)

    ax1.set_xlabel("I")
    ax2.set_xlabel("Q")

    return line1, line2, ax1  # 注意返回值，我们要更新的就是这些数据

#更新图像的函数
def animate(i):
    #注意这里必须要用global声明，不然可能出现无法动态更新数据的情况
    global gesture_i
    global gesture_q
    global update_first_flag
    global update_second_flag

    line1.set_ydata(gesture_i)

    ax3.cla()
    bar1 = ax3.bar(range(len(acc_first)), acc_first, color='rgb', tick_label=name_list)
    ax3.legend()

    ax4.cla()
    bar2 = ax4.bar(range(len(acc_second)), acc_second, color='rgb', tick_label=name_list)
    ax4.legend



    return line1, line2, ax1





def draw_view():
# 调用FuncAnimation函数生成动画。参数说明：
# fig 进行动画绘制的figure
# func 自定义动画函数，即传入刚定义的函数animate
# frames 动画长度，一次循环包含的帧数
# init_func 自定义开始帧，即传入刚定义的函数init
# interval 更新频率，以ms计
# blit 选择更新所有点，还是仅更新产生变化的点。应选择True，但mac用户请选择False，否则无法显示动画
    ani = animation.FuncAnimation(fig=fig,
                                  func=animate,
                                  frames=100,
                                  init_func=init,
                                  interval=100,
                                  blit=False)
    plt.show()


if __name__ == '__main__':
    draw_view()