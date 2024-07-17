# 本节讲解with,with是一个上下文的管理工具,在with那行的冒号后，的语句块中的操作,意味着都是在上下文进行.
# 英文中with表示"和...一起"，具有"上下文"的意象。
# 英文句子：With great power comes great responsibility.
# Python 代码：With the file opened, we can read its content.


# with open("d:/a.txt", "r") as f: 可以理解为“使用并管理 d:/a.txt 文件资源”，使得在整个 with 代码块中，文件 f 是可用的。
# 意思就是在冒号后面的语句块中，我们可以调用open打开磁盘空间的入口的文件，并且f是可用的对象。


# with 关键字引入了一个上下文管理器
# 1.准备资源:在进入时,调用上下文管理器的 __enter__方法,准备资源
# 2.清理资源:在退出时,调用上下文管理器的 __exit__ 方法,清理资源(无论是否发生了可异常)
'''
class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

with MyContextManager() as manager:
    print("Inside the with block")

可以看到with方法的实现过程:
首先是进行资源的准备,返回自身对象,然后是exit,exit中其实就包含了except缩写的exc开头的三个内容,异常类型对象,异常值对象,异常追踪对象。
exc_type,exc_val,exc_tb对象。tb是traceback的缩写
'''


with open("d:/a.txt", "r") as f:
    for line in f:
        print(line)
