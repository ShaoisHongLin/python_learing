# object类是所有类的根类，这就说明所有的类都会有object类的属性和方法,object是小写开头。


class A:
    pass
class B(A):
    pass
class C(B):
    pass

# 1. outline，在vscode中下载code outline插件,可以显示代码的大纲，可以查看大致代码里面类之间的继承关系。

# 2. C.mro也可以查看类的继承关系

'''
方法解析顺序(MRO,Method Resolution Order),结合了广度优先搜索(BFS)和C3线性化算法
Python用它来确定最终的确保在继承链中每个类只会被访问一次,避免了多继承中菱形继承的问题。
'''

print(C.mro())
# 3.dir()可以查看类的属性信息。

print(dir(object))   
'''
# 可以发现其它类的方法,也算作是object根类的属性,只不过type为<class "method">

在dir
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

 
 值得一提的是objcet根类里面,属性或者说方法，都是可以被重写的。
'''
