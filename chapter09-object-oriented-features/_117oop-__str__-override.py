# 值得一提的是objcet根类里面,属性或者说方法，都是可以被重写的，比如__str__()

#示例: 
class Student:
    '''在Student的类里面改写了它的__str__()方法'''
    def __init__(self,name):
        self.name=name
    def __str__(self):
        print("改写了str的实际功能,这样在这个Student类中使用它被重写的__str__()替代")
        pass
s1=Student("Sam")
print("123")
print(s1)

'''
1.默认使用根类的__str__,改写则使用重写的__str__(),只影响类和他的子类。

# 当我们打印print(),会隐式地调用一次括号内对象自己的"__str()__",
# 如果该实例对象的类的内部没有重写过__str()__则调用的是默认的object根类的__str__()方法

2.要重写__str__()    要return 字符串,以符合初衷

# 修改__str__()的时候,要符合__str__()方法的初衷，也就是--------最终"将返回一个字符串"。
# 如果你不写return,它不仅会对str()有影响,给对应对象的print()也会带来影响,比如Student对象内的—__str__()被改写,那么调用
# s1=Student()的"print(s1)",隐式调用__Str__的时候就会TypeError: __str__ returned non-string (type NoneType)
'''

