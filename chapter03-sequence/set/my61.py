# 集合set
# 无序、可变、元素不能重复。

# 集合的底层是由字典实现的。字典中键不能重复，所以由字典实现的集合内的元素也是不可重复的。

# 1.创建集合对象。由于集合是字典底层实现，所以也是跟字典一样的花括号，内部只放不可重复的元素。
a={3,5,7}
a.add(8)

# 2.将合适的"列表、元组"set()成为集合
a=[1,2,3,4]
b=(4,5,6)
c=set(a)
d=set(b)
print(c)
print(d)

# 3.删除、删除全部：remove()、clear()。

# a.remove()
# a.clear()


# 4.集合与数学概念：
a={3,5,7}
b={4,5,9}
# set的并、交、差 ，集合运算   (差集表示有差别的部分，去掉共同的部分。)
# a.union(b)  (或)  a|b
print(a.union(b))
# a.intersection(b)   (与)  a&b
print(a.intersection(b))
# a.difference(b)    (差)   a-b
print(a.difference(b))


