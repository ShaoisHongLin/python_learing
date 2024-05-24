# split()的讲解

# 1.split()默认按空白切割
a = 'to be or not to be'
b = a.split()
print(b)
# ['to','be','or','not','to','be']

# 2.split()可以规定按什么字符划分,但是一般还是常用上面的按空白切割
print(a.split('be'))
# ['to','or not to','']


问：python的str.split('')的返回值是什么类型？

答：python常见的str.split('')返回值是经过split分割后产生的字符串列表，是列表。