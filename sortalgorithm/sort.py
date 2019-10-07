#!/usr/bin/python3
# 文件名: sort.py

from random import randrange, shuffle

# 冒泡排序
'''
冒泡排序是最简单也是最容易理解的排序方法，其原理就是重复地走访过要排序的数列，一次比较两个元素，如果
他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成
'''
def bubbleSort(arr, order=1):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):

        # last i elements are already in place
        for j in range(n-i-1):
            if ((arr[j] > arr[j+1]) and (int(order) > 0)) or ((arr[j] < arr[j+1]) and (int(order) < 0)):
                arr[j], arr[j+1] = arr[j+1], arr[j]
            for i in range(len(arr)):
                print("%d" % arr[i], end="-")
            print("*\n")
        print("**\n")

    return

# 选择排序
'''
基本思想：第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它
与r2交换；以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。
'''
def selectSort(li):
    n = len(li)
    for i in range(n):
        temp = i
        for j in range(temp,n):
            if li[temp] > li[j]:
                li[temp],li[j] = li[j],li[temp]

# 快速排序
'''
使用了分治法策略以及递归实现，通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的
所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
'''
def quickSort(li):
    if li:
        mark=li[0]
        little=[m for m in li if m<mark]
        big=[x for x in li if x>mark]
        return quickSort(little)+[mark]+quickSort(big)
    else:
        return []

# 插入排序
'''
插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，算法适用于少量数据的
排序，时间复杂度为O(n^2)。是稳定的排序方法。插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，但将最后
一个元素除外（让数组多一个空间才有插入的位置），而第二部分就只包含这一个元素（即待插入元素）。在第一部分排序完成后，再将
这个最后元素插入到已排好序的第一部分中。
'''
def insertSort(li):
    length = len(li)
    for i in range(1,length):
        x = li[i]
        for j in range(i,-1,-1):
            # j为当前位置，试探j-1位置
            if x < li[j-1]:
                li[j] = li[j-1]
            else:
                # 位置确定为j
                break
        li[j] = x

if __name__ == '__main__':
    array = []

    # 范围内随机取12个数值
    while len(array) < 12:
        array.append(randrange(-99, 101, 3))

    # 打乱数组
    shuffle(array)

    print('排序前数组：{}'.format(array))

    #bubbleSort(array)

    #selectSort(array)

    #quickSort(array)

    insertSort(array)

    print('排序后数组：{}'.format(array))