# 类对象  、类的实例，二者的创建过程-----------了解"类具有它自己的属性".

# 1.内存分析："类对象"的创建过程。

    # class=Student之后，heap中产生类的对象. 

    # 位于heap中，类对象信息是：
    # id    
    # type=type 
    # value：《"从属于类"的属性》+方法

    # 另外class=Student的时候，栈里面也产生了Student同名的栈帧变量，指向heap中的对象。


# 2.内存分析："类的实例对象"的创建过程。

    # 利用了类的模板，s1=Student("param")之后,s1于stack中产生，指向heap中产生的实例对象

    # 位于heap中的实例对象信息是：
    # id:
    # type=Student
    # value："从属于实例的属性"+方法


# 3."从属于类对象的属性"与"从属于实例的属性"是区分开的：

'''
(一)下面这种是实例对象的属性,它们从属于实例对象。
'''
class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=Student(name="小明",age=18)
print("实例对象的使用示例,在方法中使用《实例对象属性name和age》:学生信息为姓名{0},年龄{1}".format(s1.name,s1.age))




'''
(二)下面这种是类对象的属性，它们从属于类对象
'''
class Student():
    countnumber=0
    
    def __init__(self):
        Student.countnumber=Student.countnumber+1

s1=Student()
print("类对象的属性的使用示例,在方法中使用《类对象属性countnumber》:学生总人数为{}".format(Student.countnumber))
s2=Student()
print("类对象的属性的使用示例,在方法中使用《类对象属性countnumber》:学生总人数为{}".format(Student.countnumber))
s3=Student()
print("类对象的属性的使用示例,在方法中使用《类对象属性countnumber》:学生总人数为{}".format(Student.countnumber))

