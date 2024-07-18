# OS-----Operating System 操作系统模块，我们在python中 通过该模块可以与操作系统进行沟通,调用一些操作系统的可执行文件,直接操作系统文件或者目录。

# OS对象是对于操作系统使用的，假如说我们针对一个linux的系统(windows倒是不常用),对于linux系统或者说该linux的服务器。

# 可以直接通过OS对象来对操作系统的其目录结构进行操作，或者自带的基础命令是进行运维的基础。

'''
1.导入os模块
2.通过os.system(".exe命令")  括号里面进行系统自带的基本命令
3.通过os.startfile("path") 可以启动本机器已有的该路径的软件。
'''

import os
# os.system("calc.exe") # 比如：唤醒自带的计算器
# os.system("ping www.baidu.com")
# os.startfile("C:\\QQ\\qq.exe") 
# 这里要注意对于反斜杠进行额外添加转义字符,否则会被识别为单个的转义字符



'''
4.专有符号,并不是函数,没有名字后面的()括号。

(一)
os.name是当前操作系统的名字

windows会输出"nt",这是windows在10年内的统一内核.

linux会输出posix----p是portable,os是operating system,ix是unix的后缀。代表了linux的轻便系统的特点。


(二)
添加一个当前系统的分隔符号"os.sep"

sep是separator的意思

os.sep()---------------------------跨平台的分隔符号:-----------在windows上会被识别为\       在Linux上会被识别为/
    用于兼容不同的系统,使得用python写出的路径在两种系统上都能被识别。

    如:
    path = "test_dir" + os.sep + "dir1" + os.sep + "file1.txt"可以被双系统识别。
    但是
    path = "test_dir" + '\\' + "dir1" + '\\'+ "file1.txt" 则只能被windows系统识别。

(三)
添加一个当前系统的"行"分隔符号"os.linesep()"  window上\r和\n都会被识别为换行。而linux上只有一种: \n

    
'''

print("=======================================================================================================")
print(os.name)
print(os.sep)
print(os.linesep) #输出的是换行符,是看不见的。
print(repr(os.linesep))
# repr 是representation的意思，表示展示，------"它是一个函数，返回一个对象的字符串表示，用于查看表达式的原始状态。"用于调试和检查对象的内部状态.


print("=======================================================================================================")
'''
4.os模块的文件操作

os最常用的几个操作文件的方法
os.remove(path)     删除指定文件
os.rename(src,dest)   重命名文件或目录
os.stat(path)       返回文件的状况、属性。
os.listdir(path)         返回目录下的文件
'''

print(os.stat(r"f:\123.txt"))

'''
5.os模块的目录操作

os.mkdir(path) -----------------------只能在当前工作目录或已经存在的目录中,创建一个新单级目录.如果父目录不存在,则会引发 FileExistsError 或 FileNotFoundError。

os.makedirs(path/.../.../...)----------------可以建立多级形式的目录,可以创建多层级的目录，即使某些中间目录不存在。

os.rmdir(path)--------------------删除单级目录

os.removedirs(path/.../.../...)---------------删除多级目录

os.chdir(path)----------------即cd,前往目录


os.walk()-------------------"遍历目录树".它


'''

print(os.getcwd())      # get current work directory获取当前工作目录
os.chdir("g:\\")

# 相当于linux中的cd,change directory切换工作目录     
# windows上指定盘符后还需要反斜杠来进入根路径，而写在""里面则需要再添加一个反斜杠来作为转义字符,
#如果只写成"g:"则会识别为进入了g盘但没指定路径,会进入到你上次的工作路径。而"g:\"则会报错。所以要写成"g:\\"才是G盘的根目录。

'''
在当前工作目录生成目录:
os.mkdir("123folder") 生成单级目录
os.makedirs("123folder\\test_newfoler\\subnewfolder")生成符多级目录
'''


'''
修改某目录名字:
os.rename("123folder\\test_newfoler","123folder\\改名后文件夹")
'''