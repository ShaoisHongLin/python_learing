# 列表元素访问与常用的列表对象常用的函数


# 通过索引直接访问元素：如a[2]。
a=list(['a','b','B','c','d','e'])
print(a[2]) # 结果：B
#print(a[10])  # 报错：list index out of Range

# 1.index函数的使用:“以值找索引”

'''
index(value,start,end)
index函数查找第一次出现的对应value，可以在start-end的范围里面找
'''
a=list(['a','b','B','c','d','e'])
print(a.index('a'))  # 0


# 2.count()查询元素出现的总次数
a=list(['a','b','B','c','d','e','a'])
print(a.count('a'))


# 3.len()查询列表长度。
a=list(['a','b','B','c','d','e'])
print(len(a))

