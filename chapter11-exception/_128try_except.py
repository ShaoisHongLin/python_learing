'''
Exception是程序运行过程中的不符合预期的情况,或是排查的错误。
    比如:汽车行驶过程,出现了个坑(这就属于Exception)就要安全地做出对应措施避开(属于我们要对Exception采用的措施)


    
(一)、为什么要设置Exception机制?

<1>
因为程序员也是人，在写代码时候,无法将方方面面都考虑清楚,即使没有需要错误修正的提示,也可能会有意外的错误使得代码不能通过编译。
而Exception会让程序在遇到错误时候----不会出现严重的崩溃,而是"捕获错误信息并返回"。

<2>
如果没有Exception的机制,程序员不得不将可能出现的异常情况都写在代码逻辑里,
而Exception机制的出现使得代码的逻辑跟异常分开。


(二)、Exception的类的继承关系:
Exception在万物皆是对象的python内,是所有的异常的基类,但它自身也继承BaseException类。

继承关系:
BaseException
    |
Exception
|                   |               |            |                 |                     |             
AttributeError   IndexError     KeyError      NameError         TypeError            ValueError     
对象不存在的某属性  不存在某索引  不存在某键    某变量没被定义  将操作用于不匹配的类型    接收正确类型但值错误      

 IOError                                ZeroDivisionError
 输入输出的错误操作(如打开不存在的文件)     运算中0作为除数位置

'''





try:
    print("step1")
    a=1/0
    # 下面这行step2不会被执行
    print("step2")

    #Exception使用时的关键词是except
except BaseException as e:
    print("step3")
    print(e)
    
print("step4")

'''
(三)、讲解一个单个的try except的案例

可以注意到step2不会被执行,
Exception会将程序停止并在发生错误的那一行返回,错误行之后的内容不会被执行,而转而执行except BaseException as e:里面的处理.

位于except BaseException as e后面的内容只有程序遭遇到错误才会执行,
通常会设置特定的打印输出内容,起到提示的作用作为处理方式。
'''

try:
    b=input("请输入被除数:")
    c=input("请输入除数：")
    d=float(b)/float(c)
    print(d)

except ZeroDivisionError:
    print("Error:除数不能为0")

except TypeError:
    print("Error:除数和被除数应该是数值类型")

except BaseException as e:
    print(e)
    print(type(e)) # 查看e对象的类型是哪个特定的Error.


'''
(四)、讲解一个try搭配多个except的案例

写法应该是,父类BaseException as e放在最后一个,子类的各种Error放在前面:

“先子类,后父类”
子类中先写好可以预料到的情况,再由父类接住遗漏的情况


'''