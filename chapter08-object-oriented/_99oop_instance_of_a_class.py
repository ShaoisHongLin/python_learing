# 类的实例对象

# 1.实例对象是构造方法被调用时候产生的对象。    
#               def __init__(self,param...): 
#                    self.param=param
# 2.类中的各个"method"可以通过self,访问并得到实例化之后对象的属性。
#                def print_param:
#                    print(self.param)

# 3.s1=Student(param,)       这种是执行__init__的构造方法，括号内要传递进去和init除去self之外，其它的参数，s1就是"类的实例对象"

# 创建完成后，实例对象s1具有的属性来自于__init__构造方法内的属性。

'''
另外也可以使用无参构造,即s1=Student(),特点是没有与"__init__的参数列表"保持一致,而是直接s1=Student(),区别于s1=Student(param)
'''

# 4.实例对象创造之后，可以1.在方法执行过程中，追加属性，或者2.实例对象访问属性，追加属性。
class Student:
    def print_param(self):
        print(self.param) # 访问属性


                         
s1=Student()        #无参构造
s2=Student()        #无参构造
s1.param=111         #修改属性值，
s2.param2=222        #或者用实例为s2"单独"追加新属性(不会影响其它对象或类的模板，只是为特定实例增加属性).
'''
obj.attribute = value。  
(实例)  (属性)    (值)

这里涉及到python的类具有动态特性,它可以在实例化之后的代码中修改类的构成属性,可以增加属性。
'''