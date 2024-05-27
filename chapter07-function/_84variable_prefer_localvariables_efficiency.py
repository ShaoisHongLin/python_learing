# 局部变量的引用效率高于全局变量,虽然影响不是很大，但是尽量使用局部变量

import time
a=100
def test():
    start=time.time()
    #global a-------------t=5.0
    a=100   #-----t=3.2
    for i in range(100000000):
        a+=1
    end=time.time()
    print('{}'.format(end-start))

test()