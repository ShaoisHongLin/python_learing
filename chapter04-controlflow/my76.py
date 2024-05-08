# 能熟练使用推导式是python的使用开始熟练的标识之一。列表、字典、集合、生成器(不直接生成元组)推导式。

# 推导式是利用一个或多个迭代器，配合循环或者条件句使用
# 目的是：避免重复冗长的代码出现。




# 1.列表推导式(语法)。

# [表达式 for item in 可迭代对象]

# 2.或者带条件判断的写法：
# {表达式 for item in 可迭代对象 if 条件判断}


'''
对语法结构进行解释：

1.表达式：放置一个表达式，这个表达式是最终的计算步骤，最终的结果，放到列表里面，形成你要的列表。
a=[x for x in range(1,5)]
（这里的第一个x是表达式，也可以各种计算在这里，比如下面的x*2）
a=[x*2 for x in range(1,5)]


2.最后可以加if，它先于表达式进行筛选，从可迭代对象中找到符合条件的。
a=[x*2 for x in range(1,6) if x>=5]

推导式避免的冗长：
a=[]
for x in range(1,6):
	if x>=5:
		a.append(x*2)

推导式的语法可以看出python语言风格的简洁性，以及本质是在序列里面进行迭代生成，也可以用含有迭代步骤的语言来进行，。
'''
a=[x*2 for x in range(1,6) if x>3]
b=[]
for x in range(1,6):
	if x>3:
		b.append(x*2)
print(a)
print(b)

'''
3.用在字符串中，可以将字符串拆散放入列表
a=[x for x in "abcdefghijklmn"]
print(a)
'''
a=[x for x in "abcdefghijklmn"]
print(a)


'''
4.将语法的“表达式”和 item，使用多个对象，然后迭代部分，使用2个以上序列进行并行迭代。
解释：cells是类似excel表格的单元格的含义。
cells=[(row,col) for (row,col) in zip(range(1,11),range(101,110))]
print(cells)
这样可以使得一个列表内每个位置的内容更加复杂，参考更多内容。
'''
cells=[(row,col) for (row,col) in zip(range(1,11),range(101,111))]
print(cells)