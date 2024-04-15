# 类型转化的相关知识：

# 1.混合运算中的自动转化
a = 2 + 8.0  # int + float =float
print(a)  # 10.0

# 2.四舍五入函数round
'''
它并不会改变变量的值，只是进行了一个函数的运算结果，原变量内容没变。
'''
b = 6.6
print(round(b))  # 7
print(b)  # 6

# 3.合理的类型转化
'''
类似round：还有int()
和float()
这样类型转化，也只是进行了一个函数的运算结果，原变量内容没变。
'''
c = '1'
print(float(c))  # 将c由str转化为了1.0
print(type(float(c)))  # float
print(type(c))  # str
print(c)  # 1