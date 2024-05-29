# 类(type)是用于创造对象的模板，type它自身也是对象，是类对象。

# 解释器执行到class时候，就会创建类(type)对象,类对象

class Student():
    pass
print(type(Student))
print(id(Student))
print(Student)
'''
会返回的类对象信息：
1.type信息:<class 'type'>
2.id信息:2721240604384
3.类对象的默认value信息:<class '__main__.Student'>

解释：
1.问:为什么把类对象起名为type-object,而没有叫它class object,而且对于"类对象"的type查看其类型type(Student),发现是<class'type'>,
而我们注意到,查看"实例对象"的type(s1)其类型发现是<class'object'>。

    答,我查询了chatgpt:类对象是由你提到的--"元类metaclass它是用来创建其他类的类",所以类对象会显示class<type>,而如果我把自定义的对象实例化,比如s1=Student(),那么type(s1)是class<object>,
    实例化对象对应<class'object'>,因此当我想区别《实例化对象,和类对象》时候,更应该称类对象为"type object"

类对象是对象所以也当然可以把它绑定给其它变量。

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