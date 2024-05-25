# 列表元素添加



# 1.对于append()、extend()、insert()三种添加元素的方式。加元素之后，列表扔是原来的列表，不会产生新的列表，只是列表扩长了。

'''
append('A')和extend('A')虽然略有区别，但是append和extend都直接在尾部添加，效率很高。
而insert(index,'A')自定义位置添加，添加在中间时候造成整体移动，效率较低。
'''
a=list(['a','b','c','d'])
print(id(a))
a.append('e')
print(a)
print(id(a))  # 列表对象a和append之前的id仍一样

a.extend('f')
print(a)
print(id(a))  # 列表对象a和extend之前的id仍一样

a.insert(1,'A')
print(a)      #




# 2.对于加法和乘法,这是一种较为低效率的做法，过程中产生新的列表对象,将旧列表整个拷贝到新的列表中结合。



b=list(['a','b','c','d'])
print(id(b),'这是b的id')

print(b+['e'])  # 加法直接把原数组复制过来和另一个列表对象相加
print(b*3)      # 乘法直接把原数组复制过来重复多次的新建列表对象的过程，效率会很低。

print(id(b+['e']))  # 可以发现id和a不同
print(id(b*3))     # 可以发现id和a不同
