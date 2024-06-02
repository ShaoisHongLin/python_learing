# 1.特殊方法和2.运算符的重载

# 之前介绍过__init__对应p=Person()这种运算形式的底层方法,__call__对应a()这种形式的底层。

'''
(一)特殊方法:
其实pytho中还有很多这种类似的处理:即用简单的运算符，但是运算符的底层对应着一个个特殊的方法,这些特殊方法用__method__格式作为标识。

a+b是__add__
a*b是__mult__                   multiply
a.xxx是__getattr__             getattribute获取属性值
a.xxx=value  是__setattr__        setattribute设置属性值,为属性赋值
a[]是__getitem__                    getitem获取索引项
a[]=value是__setitem__              setitem设置索引项的值
len()是__len__

print()  是__repr__和__str__
'''

'''
(二)运算符的重载:
运算符重载是指人为在某个类内修改了该类下的特殊方法,仅用于该类中。

'''

# 运算符重载示例:对一个类的特殊方法进行重写,从而在涉及该类的实例对象调用该方法时候，采用重写后的方法


class Student():
    def __init__(self,name):
        self.name=name

    def __add__(self,other):
        '''这里的other传入了一个的实例对象,对应"加号运算"右侧的操作数,对该实例对象所属类进行一个判断.
            如果传进来的是Student类的实例,那么就进行修改,如果不是,则报错'''
        if isinstance(other,Student):
            return "{0}----{1}".format(self.name,other.name)
        
s1=Student("小明")
s2=Student("小红")
print(s1+s2)
# 在该类对象作为左侧操作符时候，运算符被重载了。

print(1+1)
# 在其它的类对象的场景中,仍旧是原生的__add__方法的内容.