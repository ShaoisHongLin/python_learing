# python的面向对象的特性之---继承性

# 1.解释什么是继承性：已经发明的轮子，就没必要再造了，我们拿过来就可以稍加改动。这就是父类和子类的关系。“dont reincent wheels”

# 2.程序员对他们的称呼:父类(基类)、子类(派生类)。

# 3.python中继承的独特之处:python支持多重继承，即一个子类可以有多个父类


# 4.了解python的"根类":是这样的----"python中设定了object类为所有未规定父类的父类,是所有一切的、溯源的类就是object类。"


# 5.熟悉使用super()继承父类的定义，通过super()获取需要的属性和方法.
'''
(一)、子类的构造方法调用,以及子类获取"父类的的定义"      (之所以叫"父类的定义,是因为并不是构造方法产生的实例,而是构造方法内的属性和方法.")

例如:class Student(Person):
        pass
        
    子类构造方法的调用:
    1.子类只会调用自己的构造方法,子类对象的实例化与它父亲的构造方法无关,不论是否重写父类的构造方法,调用的都是自己的构造方法。
    
    
    子类获取"父类的的定义"
    2.子类可以在任意一个方法中,用super()对"父类的定义"进行继承,之后就可以在方法内获取到父类定义中的属性和方法了。
            语法:super(父类名,self).具体方法

            更多时候可以在单继承情况下,使用省略形式:super().具体方法
'''

# 在子类的任意某一方法中,使用super()继承父类某个内容,的例子
# 如下:
'''
示例:

首先,通过super(Person,self).__init__(self,name,age)子类继承它父类Person的__init__的方法。

class Student(Person):
    def __init__(self,name,age,score):
        super(Person,self).__init__(self,name,age)



另外,其实不涉及多继承时候可以省略为super().__init__(name, age)。

class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(self,name,age)
'''

#  super语句可以被替代,如：
# Person.__init__(self,name,age,score)
# 来继承某一方法。                      --------显式调用父类的方法，但在多继承情况下不可使用。


# class Student(Person):
#    def __init__(self,name,age,score):
#         Person.__init__(self,name,age,score)       --------(了解但不使用于多继承时候，继承某父类的方法,无法在多继承下使用)

class Person():
    def __init__(self,name,age):
        print("创建了Person类")
        self.name=name
        self.age=age
class Student(Person):
    pass

s1=Student("成年男性",36)

'''
    情景1:改写了父类构造方法,不使用父亲的构造方法.
    示例:
class Student(Person):
    def __init__(self,name,age,grade)
        print("创建了Person类")
        self.name=name
        self.age=age
        self.grade=grade

        
    情景2:改写父类构造方法,后调用父类的构造方法的定义(获取的是父类的定义,目的是得到里面的属性和方法,并不是获取实例化对象).
    示例:
class Student(Person):
    def __init__(self,name,score,grade)
        super(Person,self).__init__(self,name,age)
        print("创建了Person类")
        self.name=name
        self.age=age
        self.grade=grade
'''
# 要重点强调的的是！！！！！！super()获取的是父类的定义,目的是得到里面的属性和方法,并不是获取实例化对象
# 要重点强调的的是！！！！！！super()获取的是父类的定义,目的是得到里面的属性和方法,并不是获取实例化对象
# 要重点强调的的是！！！！！！super()获取的是父类的定义,目的是得到里面的属性和方法,并不是获取实例化对象


'''
问:继承与重写都是什么？


回答：
继承,将父类《除了"构造方法"的》"所有成员"。包括属性,方法,私有的也全部继承且可以之间调用 。

重写,是继承的基础上,获取了所有的属性方法,之后的一步,可以进行的行为,可以重新再写父类的方法做出改动进行覆盖。

'''

# mro()   可以获取到类之间的继承信息,如：Student.mro()。

print(Student.mro())



'''
多继承的具体示例:在参数列表内将“类”传入即可。
class 子类(父类1,父类2,父类3):
         类体
'''