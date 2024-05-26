# 循环语句while的语法与死循环

# 1.循环：(while)

'''
while 条件：
	s+=a
	a=a+1 # 变化着的条件用于跳出循环，另外python里面没有++ --操作。
'''

# 2.死循环
'''
while 条件：
	s+=a    
	# 变化着的条件用于跳出循环部分缺失
'''


while True:
	print("abc")
'''
while True:
	print("abc")
'''
# while True可以创建简单的死循环