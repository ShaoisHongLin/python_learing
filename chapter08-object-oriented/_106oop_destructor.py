# 析构方法__del__()与垃圾回收《垃圾：指"闲置的"、"未被引用过的"对象资源》,销毁闲置对象。


# 析构方法在python中不需要主动调用。

# 1.# python在程序尾部正常情况下会自动调用它，因为程序中每个对象都会或多或少的被引用过，python不会认为它们是垃圾。
# 当运行了所有代码之后，程序运行即将结束，这时候会对象即将消亡，被python自动调用析构函数全部清理掉。
'''
即：正常的回收时刻是程序结束的时刻进行回收,因此会在文件代码末尾调用它。
'''
# 文件末尾自动调用示例：
'''
    class Student():
        def __del__(self):
            print("调用了一次析方法")

    s1=Student()
    s2=Student()
    print("此时到底文件末尾")
'''
# 2.如果执行的代码里涉及"对象的引用被del降为0",则会被python察觉，python会"立即地",清理接下来代码中引用次数=0的对象所占用的资源，回收释放资源。
'''
即:del等语句会将对象的引用次数降为0,python会自动检测到这种"引用降为0"的对象，
'''

# 使用del,将对象的引用降为0时提前使得python提前调用析构方法示例：

class Student():
    def __del__(self):
        print("调用了一次析构方法")
s1=Student()
del s1                          # --------------------这里就会触发一次析构方法
s2=Student()
s3=Student()
print("此时到底文件末尾")
