# 如果想提高代码的效率和内存，要尽量较少嵌套循环里面的一些操作。

'''
1.减少循环内的所有计算
2.如果计算不可避免，尽量向外提
3.尽量使用局部变量进行计算，查询更快，而不是全局。


1.涉及链接字符串的时候，使用join()，而不是+
2.列表尽量在尾部进行操作，而不是中间部分。
'''
'''
v1.0   1.没有将得到固定值的内循环部分移到外循环
       2.字符串选择用加号拼接了
'''

import time
start=time.time()
for i in range(1000):
	str=[]
	for m in range(1000):
		c=i*1000
		str=str+[c+m*100]
		# str.append(c+m*100)
end=time.time()
print("耗时了：{0}".format((end-start)))

'''
v2.0   
       1.优化之处：字符串选择用append拼接了，原理上没有了新的字符串的产生
       2.缺点：固定值的计算没有放到外循环。
'''


start2=time.time()
for i in range(1000):
	str=[]
	for m in range(1000):
		c= i * 1000
		str.append(c+m*100)
end2=time.time()
print("耗时了：{0}".format((end2-start2)))




'''
v3.0   
    优化之处：1.字符串选择用append拼接了，原理上没有了新的字符串的产生
      		 2.固定值的计算放到了外循环。 
'''


start2=time.time()
for i in range(1000):
	str=[]
	c = i * 1000
	for m in range(1000):
		str.append(c+m*100)
end2=time.time()
print("耗时了：{0}".format((end2-start2)))


# 可以发现最终的耗时结果一次比一次少。