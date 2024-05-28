# 类class的定义：

# 类class就是图纸，是模板，是图纸，系统根据一个类造出的对象几乎都一样。

# class是用模板，用于创造出对象的，object----对象,instance也被称为对象，又叫做"实例"。

# instance是专门放在类与对象的区分中，因为类自身也是对象，但是类是用于创造出对象实例的，因此涉及类时候，称它创造的对象叫"实例"。

# 类内定义属性和方法:

'''
student类

class 学生:{}
    属性：
        id
        age
        name

    方法：   一般我们把"函数"拿到"类"中,就在里面叫做"方法"，就好像数据拿到类内称之为"属性"
        跑
        睡
        学
'''


'''
类名一般连在一起,不用连词符,采用驼峰原则:
    如:GoodStudent

'''

# 1.类的构造方法
class student:
    def __init__(self):
        pass
# 这里的def __init__构造方法,pass是部是空的，空语句，该方法是用于构造出这个对象。
    
# 注：self: 
#    ---类里面的任何"普通方法"，都会带一个self的量放在最前面，后面再讲解self是什么。
    
'''
    如何为构造方法传入属性
    class Student:
        def __init__(self,name,age):
            self.name=name
            self.age=age
        
    构造方法的调用:
    s1=Student('小明',19)

    这里,s1=Student('小明',19)之所以使用调用时候写Student,而不是s1=__init__(),是因为当写Student之后,
    调用类的同名时,就相当于调用该类内部的__init__()构造方法。
'''
#  而__init__（self）中的self用途，就是形如，s1=Student('小明',19)，执行构造方法将类创造出实例对象的时候，self就会成为s1对象的引用
#  构造方法被执行------构造方法产生的对象，该对象设置了参数，作为其属性------该对象还额外设置了self属性，成为实例对象的引用。
#  有了self,其它的普通方法便可以传入实例对象的引用，使用对象里面的属性了。

'''

    有了图纸就可以用它一直创造对象。
     s1=Student('小明',19)
     s2=Student('小刚',20)
     s3=Student('小亮',21)
     s4=Student('小王',19)
     s5=Student('小张',20)

'''

'''
    如何在类里面写方法：
       class Student:
        def __init__(self,name,age):
            self.name=name
            self.age=age
        def print_name(self):
            print("{0}的年龄是{1}".format(self.name,self.age))

    1.首先,类里面的其它方法也是不例外,里面要有self放在参数列表的第一个,self是
    2.其次,为什么构造方法里面要写这两句呢?不写可以嘛?
            self.name=name
            self.age=age
        如果不写对构造方法内每个函数的初始化,那么这个构造方法被实例成为对象之后,对象的属性也是未初始化的，
        在普通的方法看来,self传来的实际对象的引用中,这几个属性没被普通方法中发觉属性的生命周期，也就无法被其它普通方法使用里面的属性。
'''

# 从此往后，将最开始的对象模型在大脑里更新

# 最开始介绍python里面的对象的内存结构时候，有id type value，现在将value由简单的”值“，增进一步：
#  id 
#  type
# ------------------------------------------------------
#  value:不再是单单的值，值可以是再复杂一点的"属性+方法"结构
#     1.property属性
#     2.method方法


#如：
#   id 012354615
#   type:Student
#   property:name,age
#   method:print_name
            


'''
还有一些小知识点澄清一下：

1.python中的构造方法和C++类似,当你忘写__init__时候也可以实例化一个类,只不过只能无参构造,是因为python的类也提供了无参的__init__构造方法。

2.python中的self只不过是专门写在参数列表里。与它相同原理的是C++和Java的类中,会带有this指针,指向构造方法被执行时候，实例化出来的那个对象。
'''