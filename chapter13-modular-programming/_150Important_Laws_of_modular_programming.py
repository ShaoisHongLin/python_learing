# 这节介绍重要的模块化编程的思想，让我们不仅仅是搬运代码，而是先有一个模块的设计理念。


# 一个好的程序员不是开始就写代码。

'''
(一)先写注释设计各个API:模块要实现的功能,功能具体需要怎么的大致交互来实现。
    API需要注明函数的名称接口,需要哪些参数,注释注明如何使用。
    这个步骤可能是一个分配任务者来先写好。

(二)构思结束后再逐渐实现每个API的功能
    这个部分是程序员的主要工作内容。

(三)测试代码。并消除全局型的代码
    什么是全局性代码。比如你用于测试的打印操作,假如不用特殊的手段消除全局性的代码,
    那么其它py文件仅仅是导入该模块的时候,普通运行也会附带移植过来的模块的测试信息
    我们需要把全局性的代码放到:if __name__=="__main__":后的语句块内书写。
    
    
    之所以用__name__来进行一个文件的区分是因为:
    
        同样的模块,如果就在该模块内部:print(test1.__name__)的打印结果是__main__
        同样的模块,如果是在被导入的py文件:print(test1.__name__)的打印结果是test1
        
    所以我们对全局性的代码进行if __name__=="__main__":就只会发生在地运行自身模块的场景下,被import之后不会产生多余的字样和影响。

(四)将不希望对外部开放的函数改成私有函数
'''


'''
模块的练习：
进行模块的编写:
1.先写注释,本模块是用来干嘛的,模块的起名最好也是见名知义。
2.函数def下面一行用三个引号写好里面的功能简介。
3.在def的三个引号之间直接回车,可以生成默认的使用注释,也是很方便的。
    :parameter--用于...
    :return--用于...

'''


'''
本模块练习是用于求员工薪水的相关计算操作:
'''


daySalary=input("请输入员工的薪资")

def year_salary(monthSalary):
    """传入月薪的参数,return年薪

    Args:
        monthSalary:月薪
    """
    pass

def monthSalary(daySalary):
    """传入日薪的参数,return月薪

    Args:
        daySalary:日薪
    """
    pass


'''

另外回顾注释是可以被打印出来的,如果你导入这个模块写代码时候,忘记了该模块内具体接口该如何使用,而需要查看该方法的注释,时候

将对象的.__doc__进行打印

如print(test1.__doc__)
'''
print(monthSalary.__doc__)