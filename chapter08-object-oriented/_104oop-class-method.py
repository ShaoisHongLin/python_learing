# 类方法classmethod：静态方法。

# 区别于前面讲的内部需要传self的实例方法。

# 1.类方法是从属于"类对象"的方法，必须在def的基础上，使用装饰器@classmethod来定义类对象的方法。
# 2.类方法的参数列表里面《必须第一个写cls》,类似类里面定义的其它方法里的self，cls指向类对象本身。

# 注意：类方法的内部，不能访问实例属性和实例方法，会报错。
# 因为类方法是从属于类对象，并不是从属于类的，"模板"使用"模板的属性和方法","模板中的self传入实例的实例方法则使用实例的属性和方法""

class Student():
    name="default"
    
    def __init__(self,property1,property2):
        self.property1=property1
        self.property2=property2
    # 构造方法和其它需要传入self的方法都是"从属于实例"的方法

    @classmethod
    def print_type_object_property(cls):
        print(cls.name)
        # print(self.name)的写法注定会报错，不信可以试试。
        # 可以加深理解：类方法是属于"类对象"的方法，区别于之前使用self指向实例对象的实例方法们。

Student.print_type_object_property()