# 类的静态方法。

# 类的静态方法单独记忆即可，它和写在类外的其它方法没有区别，只是封装在类的内部，只是调用时候需要前面加上"类.方法"。

# 它虽然叫类的静态方法，它跟类几乎没密切关系，只是封装在了类内，在它名下。

# 也需要"静态装饰器"@staticmethod

class Student():
    @staticmethod
    def print_666():
        print("666")

Student.print_666()