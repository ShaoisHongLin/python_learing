# python支持在函数里面嵌套函数，即在函数里面定义另一个函数。通常把他们叫"外围函数"和"内层函数"。


#  被定义在内部的函数不能在外界被调用，只能在定义它的函数中调用,以下是基本示例：


def outer():
    print("调用了外部的函数")
    def inner():
        print("调用了内部的函数")
    
    
    inner()

outer()
# inner()则在外界无法调用。

'''
这种内部嵌套定义的函数,有什么具体的使用场景呢？
1.封装.使得外部的函数无法使用它,从基本示例就已经说明。


2.可以使得重复度高的函数被整合,用逻辑来执行各自的函数,降低代码中大量重复的而相似的部分。
'''

'''
def printChineseName(lastname,familyname):
     print('{0}{1}'.format(lastname,familyname))

def printAmericanName(lastname,familyname):
     print('{0}{1}'.format(familyname,lastname))

这两处代码重复度极高,只是改了一个打印顺序位置,逻辑重复度极高的这一行就可以被提取出来塞到更里面一层,让外层决定调用的格式。
'''

'''
def outer_print_name(country,lastname,familyname):
    # 下面两行,先对内部函数进行定义,具体怎么使用再添加外层的逻辑.
    def inner_print(param1,param2):
        print('{0}{1}'.format(param1,param2))

        
        if country=="China":
            inner_print(param1,param2)

        else:
            inner_print(param2,param1)
'''

'''
3.闭包,后面会再讲。
'''