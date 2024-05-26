# 循环语句for的语法、可迭代对象range

# 1.循环：(for)

'''
for 变量 in 可迭代对象(包括有序序列、字典、迭代器、生成器、文件对象):
	循环体

注：变量可以与循环体内配合进行输出，也可以仅仅只用意义为"遍历的次数",
比如
for x in range(5):
	print(0,end="  ")
'''

# 示例：1.字符串

for temp in "abcd":
	print(temp)

# 示例：2.对字典
d={"name":"shao","age":"18"}
for temp in d.keys():
	print(temp)

d={"name":"shao","age":"18"}
for temp in d.values():
	print(temp)

d={"name":"shao","age":"18"}
for temp in d.items():
	print(temp)

'''
d={"name":"shao","age":"18"}
for temp in d:            # 这也是遍历key
	print(temp)
'''
# 2.可迭代对象range

# range(10)就好像一个数组，没有10这个末尾。 range(10)从0-9
# range(1,10)就是1-9
# range(1,10,2)就是1 3 5 7 9

# 示例3.对rang对象:

for temp in range(5):
	print(temp,end=" ")

'''
注：变量可以与循环体内配合进行输出，也可以仅仅只用意义为"遍历的次数",不输出自身x
比如
for x in range(5):
	print(0,end="  ")
这里就没在循环体内使用x，因为有特定的内容，定义的遍历变量意义上只是遍历的次数。
'''