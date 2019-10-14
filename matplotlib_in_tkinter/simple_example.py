# simple_example
# 参考：https://www.cnblogs.com/zyg123/p/10385456.html
# 来自官网教程：https://matplotlib.org/gallery/user_interfaces/embedding_in_tk_sgskip.html#sphx-glr-gallery-user-interfaces-embedding-in-tk-sgskip-py
#
# matplotlib可以嵌入到多种gui中，包括wxpython、pyqt、tkinter等。wxpython、pyqt的显示效果更好，支持更丰富的控件，可以实现更为复杂的功能，
# 可只有tkinter是python自带的库，虽然tkinter支持的复杂控件不多，开发大工程时不太适用，但是如果支持用来开发一些示例小程序还是更为适用的。
#


# 导入tkinter模块
import tkinter

# 创建画布需要的库
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 创建工具栏需要的库
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

# 快捷键需要的模块
from matplotlib.backend_bases import key_press_handler

# 导入绘图需要的模块
from matplotlib.figure import Figure



# 实例化一个根窗口与设置标题
root = tkinter.Tk()
root.wm_title("Embedding in Tk")

# 画布的大小和分别率
fig = Figure(figsize=(5, 4), dpi=100)



# 利用子图画图
axc = fig.add_subplot(111)
axc.plot([1, 2, 3, 4, 5])

# 创建画布控件
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
# 显示画布控件
canvas.get_tk_widget().pack()

# 创建工具条控件
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
# 显示工具条控件
canvas.get_tk_widget().pack()


# 绑定快捷键函数
def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


# 调用快捷键函数
canvas.mpl_connect("key_press_event", on_key_press)


# 退出函数
def _quit():
    root.quit()
    root.destroy()


# 退出按钮控件
button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

# 消息循环
tkinter.mainloop()