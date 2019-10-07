# 参考：https://www.cnblogs.com/endlesscoding/p/10308111.html

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation


'''
更新数据点
'''
def update_points(num):
    point_ani.set_data(x[num], y[num])
    # 在不同的帧，改变了点的形状，让它在5的倍数帧显示为五角星形状
    if num % 5 == 0:
        point_ani.set_marker("*")
        point_ani.set_markersize(12)
    else:
        point_ani.set_marker("o")
        point_ani.set_markersize(8)

    text_pt.set_position((x[num], y[num]))
    text_pt.set_text("x=%.3f, y=%.3f" % (x[num], y[num]))

    # 逗号一定加上，否则动画不能正常显示
    return point_ani, text_pt,


x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig = plt.figure(tight_layout=True)
plt.plot(x,y)
point_ani, = plt.plot(x[0], y[0], "ro")
plt.grid(ls="--")
text_pt = plt.text(4, 0.8, '', fontsize=16)

# 开始制作动画
ani = animation.FuncAnimation(fig, update_points, np.arange(0, 100), interval=100, blit=True)

# ani.save('sin_test3.gif', writer='imagemagick', fps=10)
plt.show()