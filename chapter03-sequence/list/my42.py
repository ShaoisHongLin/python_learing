# 列表元素如何添加。
# 1.对于append()、extend()、insert()
'''
1.不生成新的列表对象：

append()、extend()、insert()

append('abc')和extend('abc')都可以直接在不生成新列表对象的情况下在尾部增加。

而insert(n,'abc')是在索引处添加，后面的会造成整体移动。
平常操作中，在尾部增加元素显然更推荐，因为不用整体移动，效率更高。
'''
a=list(['a','b','c','d'])
print(id(a))
a.append('e')
print(a)
print(id(a))  # 和append之前的id仍一样

a.extend('f')
print(a)
print(id(a))  # 和extend之前的id仍一样

a.insert(1,'A')
print(a)

# 2.对于加法和乘法
'''
涉及到生成新的列表对象:
+ 加号   * 乘号
复制原来对象的内容与新对象结合。
'''
b=list(['a','b','c','d'])
print(id(b),'这是b的id')


print(b+['e'])  # 加法直接把原数组复制过来和另一个列表对象相加
print(b*3)      # 乘法直接把原数组复制过来重复多次

print(id(b+['e']))  # 可以发现id和a不同
print(id(b*3))     # 可以发现id和a不同


