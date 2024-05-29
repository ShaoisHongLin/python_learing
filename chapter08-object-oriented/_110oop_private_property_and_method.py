# python的私有不是设置了一把锁头，不允许你查看，而是python作为约定，最好不要查看，可以强制查看，它没有严格的限制手段，与其它语言不同。


# 我们不设置private来强制该属性不能访问，我们只是约定俗成命名私有属性/方法，如:__name 、__play(),意思是："不建议别人进行访问"。


# 如：__name这样定义的私有属性/方法，它可以在类内部"直接"访问，但在类外部"不能直接"访问,但可以写 “  _类__私有属性或方法  ”的方式来访问。


'''

问:具体python是怎么区别对待其它属性和私有属性的?

答:python将__name的下划线变量,在解释器翻译后,增加一个前缀,"如:__name通过解释器后会变成_Student__name.

因此如果有人强行想访问时候,可以通过编写专门用来访问的代码:

Student._Student__name才能访问

'''


class Student():
    __name="default"


print(Student._Student__name)
'''
在类的外部,print(Student._Student__name)才能访问私有属性。

而print(Student.__name)不能访问。
'''


class Car():
    __CarName="大众"
    def printCarName(self):
        print(Car.__CarName)

c=Car()
c.printCarName()

'''
在类的内部,可以任意访问私有属性。
'''



'''
私有方法也同理:只能类的外面通过类似"_Student"的前缀调用该私有方法

class Car():
    __CarName="大众"
    def __printCarName(self):
        print(Car.__CarName)

c=Car()
c.printCarName()不可以访问
c._Car__printCarName()则可以访问
'''