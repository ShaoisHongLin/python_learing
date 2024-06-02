# 多态    "继承和方法重写"放在一起，就会形成多态的特点。因为它们内部都有相同的名称的方法，
# 当调用一个新的方法(对象):对象.重名方法()时候，会根据传入的对象不同,调用不同的方法

# 示例：

class Animals():
    def shout(self):
        print("发出动物特定的叫声")

class Dogs(Animals):
    def shout(self):
        print("汪汪汪")

class Cats(Animals):
    def shout(self):
        print("喵喵喵")

def Animalshout(a):
    a.shout()

Animalshout(Dogs())