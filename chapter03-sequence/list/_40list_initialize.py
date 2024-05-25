# python的列表

# 创建列表[]

# 1.创建空列表的两种方式：
    a = []
    或者
    a=list()

# 2.为列表初始化的两种方式：
a = ['0','1','2','3']
或者
a=list(range(4))

# 初次见到range(n),

# range(start end step),可以快速生成n个连续的数字从0开始到n-1，刚好对应着类似数组的索引，从0开始，表示的是个数不是实际值。

# range(5)就是生成0-4的5"个"数字。

# range的step也可以类似切片，步长设置为负数，start设置值比end还大，然后步长设置为负数，生成递减的数字。如:b=list(range(10,0,-1))

'''
c=range(10,0,-1)
type(c)
如果查看range的type，会发现它类型就称为range对象
'''

# 4.列表对象内放置字符串对象，这属于序列对象的嵌套，会将字符串对象的内容以最小单位拆解。

'''
a = list('a123,66a')
print(a)

'a','1','2','3',',','6','6','a'
'''
