# 这节讲 try—except——else之后继续加上finally，这个finally的意思是为try--except增加

# finally的作用是，不论是否发生异常，均会执行的内容。
# finally的主要用途是，操作结束后，释放该释放的资源。
try:
    f=open("F:/a.txt","r")  # open函数，专门用于打开本电脑的磁盘文件，打开磁盘中的文件并返回一个文件对象
    '''
    在这里提及一下open()函数,open用于跟操作系统沟通,并打开磁盘的传输通道,
    第一个参数是文件名,第二个参数是r(read)/w(write)/a(add尾部追加)模式,后面还可以加encoding="utf-8"来设置字符集编码方式。
    '''
    content=f.readline() #文件对象可以进行readline()读取一行内容
    print(content)
except BaseException as e:
    print(e)
finally:
    f.close()  # 每次文件对象被open函数打开，就相当于建立了操作系统与硬盘的通道，我们需要后面把通道关掉。


'''
讲解一下return。

我们平常写try except经常是用于函数体内,常常容易发生错误的地方,对即将到来的错误采取处理措施而使用异常机制。

往往try except使用在,文件对象的打开,数据库对象的连接等需要打开关闭的内容中。
其中就涉及到一个问题-----函数进行基本逻辑和try except,return写在哪?可以写在try except里面吗?
答案是-======不可以的.

try except只是先探错的过程,
而在里面return却是实实在在的返回了,
会毁掉整个try except的本来作用,
也往往会导致返回后不再执行finally进行的资源释放的工作

谨记:return放在方法的最后
'''