# python中对于重载Overloading的问题解决策略。

# 重载Overloading问题：是指的高级语言中，遇到《同名、不同参》的处理方式


'''
重载Overloading在C++和Java中的处理:当使用同名不同参的时候,会根据传入参数的不同,识别为各自独立的函数。

重载Overloading在python中的处理:当使用同名不同参的时候,python不会分辨参数列表是否不同,同名的函数只能载入最后载入的,
取代前面的同名函数,即使参数列表不同,"后载入的同名函数"也会覆盖取代"先载入的同名函数"。
'''
# 多个重名的方法在python中会被取代，只有最后一个载入的有效。


class Student():
    def printHello_method(self):
        print("Hello")
    def printHello_method(self,param1,param2):
        print("Hello")

s=Student()
# s.printHello_method()
s.printHello_method()


'''
无参的printHello_method由于python的重载的特性,写过printHello_method(self)，
但是载入时候被另一个同名函数printHello_method(self,param1,param2)取代了,调用时候会报错。
TypeError: Student.printHello_method() missing 2 required positional arguments: 'param1' and 'param2'
'''
