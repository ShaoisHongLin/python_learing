# 异常类除了python提供给我们的，如果实在有需求，我们可以自己定义异常类，虽然使用的场景很少。

# 听起来复杂，其实只需要继承Exception这个基类，然后在初始化时候传入一个ErrorInfo的对象用于存放错误信息
# 再修改你指定的__str__以便于按你自定义的要求打印出来错误信息即可。

class MyException(Exception):
    def __init__(self,ErrorInfo):
        Exception.__init__(self)
        self.ErrorInfo=ErrorInfo
    def __str__(self):
        return str(self.ErrorInfo)+"产生了我自己定义的错误"
    

# 下面的代码时做出一个测试
if __name__=="__main__":
    age=int(input("请输入一个年龄"))
    if (age<1 or age>110):
        raise MyException(age)
    else:
        print("正常运行，没有产生错误")

'''
PS G:\Git\mingw64\GitVault_all\python_learning> & G:/Python/python.exe g:/Git/mingw64/GitVault_all/python_learning/chapter11-exception/_134user-defined_exception.py
请输入一个年龄15
正常运行，没有产生错误


PS G:\Git\mingw64\GitVault_all\python_learning> & G:/Python/python.exe g:/Git/mingw64/GitVault_all/python_learning/chapter11-exception/_134user-defined_exception.py
请输入一个年龄-1
Traceback (most recent call last):
  File "g:\Git\mingw64\GitVault_all\python_learning\chapter11-exception\_134user-defined_exception.py", line 18, in <module>
    raise MyException(age)
MyException: -1产生了我自己定义的错误
'''