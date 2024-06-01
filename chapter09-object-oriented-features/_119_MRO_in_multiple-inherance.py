# 另外介绍多继承中，传递参数列表时候，假设有重名方法，它会按由左到右侧的优先级来决定的，这是   MRO （Method Resolution Order） 

'''

前面提到了这个MRO方法,

1.MRO机制的作用:第一次我们知道  <class>.mro() 可以对类使用,用于查看该类的继承层次关系,用它来避免了类的重复引用的问题,确保同一个类继承中只引用一次。

2.MRO method resolution Order方法解析顺序,正如其名,它更多的作用是在多继承中的重名的方法,决定采用从左到右的优先级,优先选择左侧的方法调用。

多继承如:Student(ChinesePeople,AmericanPeople)的两个参数,ChinesePeople和AmericanPeople都有同名的方法,如

'''
class ChinesePeople():
    def eyesColoris(self):
        print(" ChinesePeople黑眼睛")


class AmericanPeople():
    def eyesColoris(self):
        print("AmericanPeople蓝色或其它颜色眼睛")


class Student(ChinesePeople,AmericanPeople):
    pass

s1=Student()
s1.eyesColoris()
print(Student.mro())


# 上面代码中，最后会输出ChinesePeople内部的eyesColoris的属性，这其实是由于MRO机制决定的，这其实是它的主要使用场景以及解决的问题，

# 即：它用于解决多继承中的重名方法冲突时候，采用从左到右优先级的调用方式。

# 另外mro的使用语法是:类.mro() ,比如：Student.mro()而不是S1.mro()