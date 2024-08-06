# 如果我们点ctrl并且查看某个比如Button的源码，往往会注意到它继承了一个或者多个类。

# 对于Gui编程，它内部主要记住几个分支就可以。


'''
1.最为主要的"组件分支",Basewidget继承了misc(miscellanous--"杂项")、pack(盒模型定位)、grid(表格定位)、Place定位,而Basewidget下面又有widget里面是Button、Label和更多内容.

2.Toplevel--toplevel是最顶层的弹窗级别,如果不先对其进行交互,则无法对其它窗口进行交互,比如报错的强烈提示.
    Toplevel继承的是Basewidget、Misc

3.Tk--Tk继承了Wm(window manager窗口i管理器)
'''

'''
但这些也不是必去掌握的.可以通过ctrl进入一个类的源码,并右键类名选择diagram查看图解.


'''


'''
"父容器"与"组件"的解释

编程中,对于数据的结构,可以叫做parent和child的父子关系.
但是对于组件式编程,我们要体现组件之间的层次关系,往往将父子关系叫做master 和slave,一般提及master就要想到是类似"父容器"的意思.要迅速掌握这一思想,不要感到生僻。

组件,我们提到GUI编程中最为重要的那一分支,就是各种组件Button,Label,Canvas,Frame...

这些都是组件,一个组件的实质是一个类,
    我们比较需要掌握的就是---------------"类的参数列表"需要传入"父容器".比如btn01=ttk.button(root...)证明button组件要安置在root的父容器下.

我们在下节:会示例一个使用面向对象编写的最为基本的GUI的示例,就是通过自定义了一个Application,它是以"我们自定义组件的形式",
Application这个类中,将涵盖所有我们要实现的步骤以设计一个GUI的程序,并将其父容器进行mainloop实现.
'''

