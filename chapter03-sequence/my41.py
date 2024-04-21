# range的推导式生成

a=[x*2 for x in range(5)]
print(a)
# 如何去看这个长串?
'''
for代表着循环操作，看它右侧是对一个0-4的range对象进行循环，for左侧是对其进行的循环指令：x*2。
'''



# 还可以继续加上if在这个长串内筛选。
b=[x*2 for x in range(50) if x%4==0]
print(b)
