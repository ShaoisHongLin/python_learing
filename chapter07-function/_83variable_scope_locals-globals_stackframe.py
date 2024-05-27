# 变量的作用域：

'''
    全局变量：
        在函数外部声明的变量，整个文件(或在python中叫模块),从定义起到模块结束，都是它的作用范围。
        尽量少使用全局变量,会影响函数的一致性和通用性。
        

    局部变量：
        局部变量在函数内部声明。
        局部变量的引用效率高于全局变量。
        局部变量在函数内优先级别大于全局变量。

        
    如果一定要在函数内部使用全局变量,并对其产生全局性修改，那么就要先写一行声明,如:global a

    a=1
    def f1():
        global a
        a=5
        return a
    
    f1()
    print(a)------a=5
'''

'''
    内存分析----函数以及栈帧。
        函数名的本身在定义之后,就是以全局变量的形式存在于stack中,
        当该函数执行时,开辟stack的一块连续的"栈帧"，在里面产生内部的局部变量,在整个函数结束时候栈帧消失。
'''


'''
    介绍两个函数：
    locals()和globals()
    在函数中打印它们,可以获取到函数内的本地变量和全局变量。

'''

def variables():
    '''
    利用locals()打印函数内部的本地变量,以及global()打印全局变量
    '''
    print(locals())
    print(globals())

variables()

'''
可以发现,全局变量都是双下划线的,如'__doc__','__file__',的样子.
你还可以找到variable本身:'variables': <function variables at 0x0000027738148A40>},说明"函数名"也是全局变量中的一员。
'''