# 循环语句的嵌套:

# 题目：利用for循环输出图案：
'''
0 0 0 0 0
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
'''
for x in range(5):
	print(0,end="  ")
print()
for x in range(5):
	print(1,end="  ")
print()
for x in range(5):
	print(2,end="  ")
print()
# 当我们注意到代码有着几乎一模一样的部分。证明代码写的很繁琐，是可以优化的，如：
for x in range(5):
	for x in range(5):
		print(0,end="  ")
	print()


'''
注：变量可以与循环体内配合进行输出，也可以仅仅只用意义为"遍历的次数",
比如
for x in range(5):
	print(0,end="  ")
'''