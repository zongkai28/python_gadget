import pida
import matplotlib.pyplot as plt

plt.figure(1) # 创建图表1
plt.figure(2) # 创建图表2
 
#测试PID程序
def TestPID(P, I, D):
    IncrementalPid = pida.IncrementalPID(P, I, D)
    PositionalPid = pida.PositionalPID(P, I, D)
    IncrementalXaxis = [0]
    IncrementalYaxis = [0]
    PositionalXaxis = [0]
    PositionalYaxis = [0]
 
    for i in range(1, 500):
        #增量式
        IncrementalPid.SetStepSignal(100.2)
        IncrementalPid.SetInertiaTime(3,0.1)
        IncrementalYaxis.append(IncrementalPid.SystemOutput)
        IncrementalXaxis.append(i)
 
        #位置式
        PositionalPid.SetStepSignal(100.2)
        PositionalPid.SetInertiaTime(3,0.1)
        PositionalYaxis.append(PositionalPid.SystemOutput)
        PositionalXaxis.append(i)
 
    plt.figure(1)      # 选择图表1
    plt.plot(IncrementalXaxis, IncrementalYaxis,'r')
    plt.xlim(0,120)
    plt.ylim(0,140)
    plt.title("IncrementalPID")
 
    plt.figure(2)     # 选择图表2
    plt.plot(PositionalXaxis, PositionalYaxis, 'b')
    plt.xlim(0,120)
    plt.ylim(0,140)
    plt.title("PositionalPID")
 
    plt.show()
 
if __name__ == "__main__":
    TestPID(4.5,0.5,0.1)
