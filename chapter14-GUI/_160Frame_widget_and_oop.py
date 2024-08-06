# 本节先讲Frame组件的使用以及oop面向对象的写法写GUI程序,以扩展规模。

'''
Frame组件是相当于虚拟的方框,可以理解为“容器/框架”组件,是一片矩形的区域,Frame组件的作用就是规划区域,通俗来讲就是先圈出一块地,以用于在这片地上展开各种组件的设计。

往往固定地我们先创建一个tk对象,叫做root,作为我们实际使用中放在规划区域内的最大的那个实体窗口,
在Application类中,写这个Application内部的具体实现细节,用到哪些组件之类的内容...
最终,将root作为Application的父容器传入这个参数列表.

Frame 组件本质上是一个矩形区域，可以包含其他组件（如按钮、标签、文本框等），并且可以嵌套以创建复杂的布局。

'''

from tkinter import *
from tkinter import messagebox

# 知识回顾:这里的Frame是继承,别脑子不转弯认为是函数的参数列表了,这里可不是函数。
class Application(Frame):
    '''一个最为经典的GUI程序的写法示例,定义一个App类,然后将容器设置为参数。这样继承一个组件就相当于在组件内搞一个Application组件'''
    
    def __init__(self,master=None):
        '''构造函数,每个类都必须有的,用于将类实例化。
        值得注意的是需要在参数列表中,手动设置一个master对象,以配合后面app组件传入master进去.
        要使得自己定义的Application成为类似Frame的组件,需要主动调用父类的构造方法super().__init__()并且ctrl点进__init__查看必要的参数列表.
        
        此时self是什么?
        是Frame组件----身为组件,可以作为其它组件的父容器传入参数列表.
        '''
        super().__init__(master)  # 使用super的init时候不用再传入self,但要传入其他必要参数
        self.master=master    # 将master也就是root赋值给继承父构造方法中的参数列表中的master
        self.pack()         # 采用盒子模型来布局root,每个组件都要设定布局方式之后才能在界面中显示出来，
        self.createWidget()     # 开始初始化各种组件
        
        
    def createWidget(self):
        '''开始初始化各种组件'''
        self.btn01=Button(self)
        # 属性1作为新增的变量:btn01
        self.btn01["text"]="点击此处按钮.触发特定函数"
        self.btn01.pack()
        self.btn01["command"]=self.f1
        '''
        上面展示的是button的分行散开写,也可以=Button(都写到这个括号内)
        '''
        self.btn02=Button(self,text="关闭",command=root.destroy)
        '''
        command这里是root.destroy,哪个组件+destroy就可以结束销毁哪个组件.destroy的底层是进行了一个遍历将所有的组件进行销毁。
        '''
        self.btn02.pack()
        
    def f1(self):
        messagebox.showinfo("弹窗","这里显示弹窗的文字")    # 弹窗的标题和弹窗的文字.
        # 疑问：这里为什么import tkinter * 没有将tkinter的messagebox也导入进来呢，
        # 原因是之前学过的内容:tkinter这一package里面__init__.py里面没有写messagebox的导入语句
            

# 写容器里面的各个组件,先创建tk对象,再调用tk对象中的组件.
root=Tk()
root.geometry("960x540+300+200")
root.title("这是最简单的GUI中的app对象的示例")
# 把前面的容器作为参数,放入我们自定义的类里面。
app=Application(master=root)  # 这里的master是GUI编程里面的独特的从属关系，称之为Master 和Slave,主和奴仆的关系
root.mainloop()