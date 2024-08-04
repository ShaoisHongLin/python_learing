from tkinter import *             # 导入tkinter的传统包中所有内容
from tkinter import messagebox
from tkinter import ttk              # 导入tkinter的新版包ttk


'''

(一)、初识,建立出一个可视的窗口

root = tk.Tk()                              

# class tkinter.Tk(screenName=None,baseName=None,className='Tk',useTk="True",sync="False")
# 首先要根据tk对象的设定,建一个tk对象的实例,第一个"是字符串"的参数将被对应上className参数,被识别为"类的实例名字".

root.mainloop()
# 这里
'''

'''

(二)、认识基本的几个组件
1.tk.grid()是布局管理器,是将内容以网格布局的方式来进行,类似html中表格布局的布局方式.

2.Frame是布局用的.看不出来但是会根据类似表格的方式使得下面的grid column和row可以布局。

tk.grid(column=,row=,)-----设置在父窗口中子组件的位置,以表格的单元格位置作为落点.column和row类似数组索引,从0开始是第一个位置.然后是1、2.
注意:grid()返回的对象是None值,不要链式使用如“label=Label(tk_parent,text="").grid()后赋值给变量,这是把None赋值过去了,要分开写”

3.Label(tk_parent,text="")文字框,返回一个该的组件的tk对象。
4.Button(tk_parent,text="")按钮,返回一个该类组件的tk对象。


如:
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
label01=ttk.Label(frm, text="Hello World!")
label01.grid(column=0, row=0)
btn01=ttk.Button(frm, text="Quit", command=root.destroy)
btn01.grid(column=1, row=0)
root.mainloop()

再顺便介绍pack(),动词打包,意味着成盒子,即css的盒模型
pack()和grid()都是布局的方式,pack是盒子的布局方式,二者只能二选一.
'''

root =Tk()            # 创建tk的应用程序对象,并为对象起名为root,大致表示的意思是根窗口对象
frm = ttk.Frame(root, padding=10)     # 在根窗口对象内使用ttk.Frame,只有规定了Frame,在Frame对象内的grid()布局才会若我们所想一致
# Frame里面还可以套frame进行嵌套的布局.
frm.grid()
label01=ttk.Label(root, text="Hello World!")# 文字标签组件
label01.grid(column=0, row=0)# 第一列,第一行
btn=ttk.Button(root, text="退出", command=root.destroy)  # 第二列,第一行
btn.grid(column=1, row=0)
root.mainloop()

'''
(三)、实现交互弹窗,学会监听事件

首先要注意:每有一个tk对象,就要设定一次布局,无论你想用grid()还是pack()

编写函数.并在函数的参数位置设置一个event
    写函数内的事件

将函数绑定在一个tk对象上:
    对tk对象,用bind()进行绑定,bind的第一个参数是"按键如<Button-1>",比如button1表示左键,经常玩游戏的可能都知道,如何第二个绑定给"触发函数函数"
'''


root1=Tk()
frm1 = ttk.Frame(root1, padding=10)
frm1.pack()             # 每有一个tk对象,就要设定一次布局
btn2=ttk.Button(frm1, text="点此按钮触发函数interact_message", command=root1.destroy) 
btn2.pack()
def interact_message(e):
    '''事件的函数,里面的参数对象是一个event对象,我们要将这个事件设计为弹窗,顺便取名为interact_message'''
    messagebox.showinfo("Message","弹出提示信息")
    print("触发了一次点击弹窗message")
    
btn2.bind("<Button-1>",interact_message)        
root1.mainloop()