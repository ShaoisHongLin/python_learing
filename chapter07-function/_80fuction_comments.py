# 定义函数时候，加上文档字符串是很好的习惯，其次，文档字符串可以被两种方式输出出来以方便查看
def add(a,b,c):
    '''add函数功能是a+b+c,返回值是sum'''
    sum=a+b+c
    return sum
'''
查看函数的文档字符串的两种方式：
1.help(add)    
2.help(add.__doc__)


如果提示'more' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

那么需要你在本机的环境变量Path里面加上
%SystemRoot%\System32\即可
'''

help(add.__doc__)