# @property装饰器

# @property可以将一个方法的调用方式变为"属性调用"

# @property可以帮助处理属性的读、写操作，对于一个属性，如:s1.salary=30000的操作是不安全 的

# 本能想出的代码读操作：s1.salary访问属性
# 本能想出的代码写操作: s1.salary=访问属性并赋值

'''
如果这是一个salary()那么它就可以限制该属性的范围,比如3000-9000rmb,但是对于属性而言.如果有人将它赋值9999999999也没有逻辑阻拦它.

@property声明方法作为属性,那么这个属性是由一个方法改造而来,方法改造而来的属性,将更加灵活性,可以加入逻辑的处理操作.

在读取时候可以有很大优势。
'''


'''
场景1:通过将"实例函数返回实例对象的属性值"的改造,用@property改造为一个属性,可以建立"只读"属性。
也就是只能读取实例对象的属性值返回,而不能进入修改,即可达到C++中的private属性的等同效果
'''
# 示例：由python的“假私有属性"和"property声明的<只返回>函数"，模仿C++的private只读属性


class Student():
    def __init__(self,score):
        self.__score=score
    @property
    def score(self):
        return self.__score
sam=Student(59)
print(sam.score)# 可读取
#sam.score=100     没设置setter的代码,则不可写入,是仅读。
'''
场景2:写入的增强版，写入属性的时候，只需要声明   @函数名.setter,就可以搭配@property的函数进行setter的操作。

但它又不单单是对C++的private的拙略模仿,而是可以对其进行逻辑限制,比如为写入操作设定逻辑限制其范围.让该@property创造的属性自带逻辑处理,更加灵活

通过@property和@函数名.setter,python中的读取和写入操作分离开,
'''
# 示例：将一个属性内部设有逻辑判断:


class Employee():
    def __init__(self,salary):
        self.__salary=salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,salary):
        if 5500<salary<6000:
            return salary
        else:
            return self.__salary
Li=Employee(5900)
print(Li.salary) 
Li.salary=5800 # 用setter设定了一定的可修改范围

'''
对比一下,可以发现.C++的类通常不是以直接实例化传入方法中，因此要设置对应传入的参数、规定参数的类型、以及实例化一个对象的生命周期规定内存规划、异常处理、
代码中符号连着符号,get、set函数的名称通常很长难以阅读,对程序员来说耗费大量精力处理琐碎的简单的变量做很多规划、回头阅读时候也冗长难以维护,
而python程序员能更轻松地完成类似的规划直接注重在业务功能上。
'''

