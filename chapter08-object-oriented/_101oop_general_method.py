# 除了用户自定义的方法，还有些python自带的方法：

# 1.dir()或者dir(实例对象),获取所有的属性方法，或者获取某特定实例对象的属性、方法。获取到一个list里面。
print("-----------打印一下dir方法的返回值类型---------")
print(type(dir()))



print("-----------打印一下dir方法直接使用的结果:python自带的一些内置属性方法---------")
print(dir())


print("-----------打印一下dir方法对实例使用的结果:实例对象的属性和方法---------")
class Student:
    def __init__(self,name):
        self.name=name
a=Student("shaohl")
print(dir(a))


# 2.obj.__dict__,可以获取对象的全部属性，以字典形式返回。
print("-----------打印一下.__dict__方法的返回值类型,确认是<clas:'dict'>---------")
print(type(a.__dict__))


print("-----------打印一下.__dict__方法对实例使用的结果:返回实例的属性,以字典格式---------")
print(a.__dict__)

# 3.isinstance(obj,class)，查看该实例是否是特定的属性，返回布尔值。
print("-----------打印一下isinstance(obj,class)的使用---------")
print(isinstance(a,Student))

'''
输出结果：
-----------打印一下dir方法的返回值类型---------
<class 'list'>

-----------打印一下dir方法直接使用的结果:python自带的一些内置属性方法---------
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

-----------打印一下dir方法对实例使用的结果:实例对象的属性和方法---------
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name']

-----------打印一下.__dict__方法的返回值类型,确认是<clas:'dict'>---------
<class 'dict'>

-----------打印一下.__dict__方法对实例使用的结果:返回实例的属性,以字典格式---------
{'name': 'shaohl'}



True
'''