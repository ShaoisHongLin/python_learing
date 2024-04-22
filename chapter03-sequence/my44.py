# 列表元素访问与计数


# 1.通过索引直接访问元素：如a[2]。
a=list(['a','b','B','c','d','e'])
print(a[2]) # 结果：B
#print(a[10])  # 报错：list index out of Range

# 2.index函数的使用:“以值找索引”

'''
index(value,start,end)
index函数查找第一次出现的对应value，可以在start-end的范围里面找
'''
a=list(['a','b','B','c','d','e'])
print(a.index('a'))  # 0


# 3.count()查询元素出现的总次数
a=list(['a','b','B','c','d','e','a'])
print(a.count('a'))


# 4.len()查询列表长度。
a=list(['a','b','B','c','d','e'])
print(len(a))

# 5. 20 in a 关键词in来判断列表里是否有某个元素
a=list(['a','b','B','c','d','e'])
print('a' in a) # True

