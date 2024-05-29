# 类(type)是用于创造对象的模板，type它自身也是对象，是类对象。

# 解释器执行到class时候，就会创建类(type)对象,类对象

class Student():
    pass
print(type(Student))
print(id(Student))
print(Student)
'''
会返回的信息：
<class 'type'>
2721240604384
<class '__main__.Student'>


print(Student)的结果是<class '__main__.Student'>,可以发现类对象的默认值是<class '__main__.>,由于是对象,

类对象甚至赋给其它变量,

比如:
a=Student     a绑定了一个类对象的id
s1=a()        s1也绑定到了a对应的id,那么这一行可以看作:a=Student(),调用无参构造了。
这样
'''

# 值得一提的是，现在没怎么过使用def __new__():,主要使用了def __init__()构造对象。

# def __new__()是用于复制出n个"类的实例"，如果使用__new__()，它们会《引用》同一个"类对象"，它们共享同一个类对象的地址，这也说明了类是对象。



# s1---------------->      引用Student的id
# s2---------------->      引用Student的id
# s3---------------->      引用Student的id