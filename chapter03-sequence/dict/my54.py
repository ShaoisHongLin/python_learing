# 字典是键值对的"无序"、"可变"序列，以键值对(key-value)存在。

# 序列中，list使用"下标数字"找到对象，dict使用"键(key)"找到对象

# dict是可变序列对象其中之一。

# 键是不可变对象，不可以用set、dict、list这三个可变对象来作为键。。


'''
1.普通创建一个dict对象,用花括号，内部的键一般用字符串，键值之间用冒号。
多半是使用一个字符串，比如'name'
'''
a={'name':"shao",'age':18,'score':90}

# a={} 空字典对象

'''
2.显式地用dict函数创建dict对象，
第一种：少量内容的写法(一行那种)，此时格式规定不用字符串的引号，键和值之间用等号。
dict(name="shao",age=18,score=90)
'''
a=dict(name="shao",age=18,score=90)
print(a)

'''
第二种：较多内容的写法(用中括号和小括号相隔、每个小括号内左边键，右边值，中间逗号、键用引号)
b=dict([(),
        (),
        (),
])
'''
b=dict([("name","shao"),
        ("age",18),
        ("score",80),
])
print(b)

# b=dict()空字典对象


'''
3.通过zip(k,v),配对函数,创建字符串.
k=["name","age","money"]
v=["shao","18","95"]
d=dict(zip(k,v))

'''

k=["name","age","money"]
v=["shao","18","95"]
d=dict(zip(k,v)) # 将迭代器zip配对后的对象变为dict对象
print(d)
print(d)

'''
4.dict的字典对象，formkeys，用于创建空的新字典对象。

dict.fromkeys(["name","age","score"])
'''
f=dict.fromkeys(["name","age","score"])
print(f)  # {'name': None, 'age': None, 'score': None}
