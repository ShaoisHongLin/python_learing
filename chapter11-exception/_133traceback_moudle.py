# 如果一个程序要跑很久，或许是一个晚上，第二天再看。

# 我们可以利用traceback模块，使得异常信息打印并输出到日志里面。

import traceback

try:
    num=1/0
except:
    with open("f:/a.log","a")as f:
        traceback.print_exc(file=f)


'''
Traceback (most recent call last):
  File "g:\Git\mingw64\GitVault_all\python_learning\chapter11-exception\_133traceback_moudle.py", line 8, in <module>
    num=1/0
        ~^~
ZeroDivisionError: division by zero
发现a.log文件里面出现了这样的异常信息。
'''