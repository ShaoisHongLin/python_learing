# 利用生成器，推导式创建元组。

'''
1.推导式生成的是生成器(generate)对象

先回顾列表的推导式生成list()
a=[x*2 for x in range(4)]
只不过元组用括号
a=(x*2 for x in range(4))
二者生成的不是list或tuple对象，而是生成器对象

生成器对象可以转化成其它对象并用来"迭代遍历"（输出），仅一次,之后就会变成空对象
'''
a=(x*2 for x in range(4))
print(type(a))
b=tuple(a)
print(b)   # (0,2,4,6)
c=tuple(a)
print(c)   # ()

'''
问：为什么生成器对象不论是转化成tuple还是直接用生成器的__next__()遍历只能遍历一次？
因为：生成器对象有一个指针，放在最开头，如果对这个生成器对象施加操作，它会利用指针移动，直到最末尾。
当再次访问，它无法自己移动到最开头。
'''

'''
2.用__next__()移动指针，这样不必转化为形式上的tuple，直接通过指针使用生成器。
'''
e=(x*3 for x in range(3))
print(e.__next__())
print(e.__next__())
print(e.__next__())
# print(e.__next__())  这行会报错，因为指针已经到达结尾。 Stop Iteration