# python的列表

# 创建列表[]
# 1.以比较不明显的方式创建列表
a = ['a', 'b', 'c', 'd']
b = []

print(a)

# 2.以比较明显的方式创建列表
a = list()  # 创建一个列表对象。

# 3.range()配合列表的使用
a = list()

b = list(range(10))  #
print(b)
# range(n)   可以快速生成n个连续的数字从0开始到n-1，刚好对应着数组的实际索引
'''
range的详细用法，跟切片差不多，是range(start,end,step),默认为(0,n,1)

步长负数也可以倒序。
'''
c=range(10,0,-1)
type(c)
d=list(range(10,0,-1))
print(d)



# 4.字符串配合列表的使用：逐个拆解

a = list('a123,66a')
print(a)