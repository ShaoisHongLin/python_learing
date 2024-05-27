# time模块

'''
知识点：
time模块是根据unix操作系统时间的起始来算的，也就是1970年的一开始。
最原始的time.time()获取的是从1970年一月一日0:00到现在经过的确切秒数，是一个float精确到了毫秒，进行int(time.time())则是秒数
'''

import time
print(time.time())   # 获取此时此刻，距离unix系统时间的float值

print(int(time.time()))


'''
假如我们想看一个算法的时间：

在函数的开始时候:
start=time.time()


程序快结束的时候:
end=time.time()

print('{1}是程序运行的时间'.format(end-start))
'''
