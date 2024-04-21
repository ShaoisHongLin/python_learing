# 列表元素如何添加。


# 列表对于在尾部添加数据十分推荐，一般情况在尾部添加，因为整体移动会降低效率。



# 1.对于append()、extend()、insert().
'''
不生成新的列表对象：

append()、extend()、insert()
它们三个作用一模一样，都是近义词，作为同一功能。
它们三个对比加号添加合乘号添加，真正添加在原来的对象内。
'''
a=list(['a','b','c','d'])

a.append('e')
print(a)
print(id(a))

a.extend('f')
print(a)
print(id(a))
'''
涉及到生成新的列表对象:
+ 加号   * 乘号
复制原来对象的内容与新对象结合。
'''
a=list(['a','b','c','d'])
print(id(a))
print(id(a+['e']))
print(a+['e'])