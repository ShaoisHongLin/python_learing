# 本节讲解Label组件，Label组件上可以有文本，gif，背景图片，颜色等内容。
'''
Label

def __init__(self, master=None, cnf={}, **kw):

STANDARD OPTIONS

            anchor (单行文本的对齐,e右侧,w左侧,center),
            highlightthickness, image, justify(非单行文本对齐),
            background, (背景色,是视图容器的背面/底层的颜色), 
            foreground,(前景色,是视图容器的表面的颜色,比如黑背景下的白色字体,那么foreground就是"white"), 
            bitmap(位图,用像素产生的类似图片的数据结构),
            font(字体),
            
            activebackground
            activeforeground
            borderwidth, 
            cursor,
            disabledforeground,
            highlightbackground, highlightcolor,
            padx, pady, relief, takefocus, text,
            textvariable, underline, wraplength

        WIDGET-SPECIFIC OPTIONS

            height, state, width
'''
from tkinter import *

class Application(Frame):
    
    def __init__(self,master=None):
        super().__init__(master)   # 在声明构造方法的同时新建一个"master变量",接收root对象,并直接传入到父类的构造方法参数列表里面的master
        self.master=master
        self.pack()
        self.createWidget()
        pass
        
    def createWidget(self):
        self.label01=Label(self,text="标签名",width=10,height=2,background="blue",foreground="white",anchor="center",
                            font=("黑体",15))                           
        #此处self指代的实例对象就是由root作为master构建出的父tk容器
        self.label01.pack()
        
        # 接下来开始尝试在标签中加入图片,先规定变量PhotoImage(),再用Label里面的image属性。
        '''
        这里的photo不能被定义成局部变量,因为mainloop一直循环时候在photo作为局部变量生命周期结束之后不会显示出来它,因为它刚好在这部分代码结束之后消亡.
        
        global photo
        
        photo=PhotoImage(file="arrow.gif")
        
        self.label02=Label(self,image=photo)
        
        self.label02.pack()
        '''
        global photo
        photo=PhotoImage(file="chapter14-GUI/luffy.gif")  # 这里要写项目下的文件夹下的文件
        self.label02=Label(self,image=photo)
        self.label02.pack()
        
        self.label03=Label(self,text="多行文字1\n多行文字2\n多行文字3",borderwidth=10,relief="ridge",justify="left",font=("宋体",25))
        
        # 这里之所以relief一词表示动画效果,就是因为relief在艺术界是浮雕的意思,用带有层次的凸起凹陷等手法使之塑造形象。
        '''
        "solid"：实线边框。
        "flat"：无边框，平面效果。
        "raised"：凸起效果，使控件看起来像从界面上突出,类似未按压下去的的扫雷格子。
        "sunken"：凹陷效果，使控件看起来像是嵌入在界面中,类似按压下去的扫雷格子。
        "groove"：边框呈现凹槽状,边框像是被挖了一周的沟槽。
        "ridge"：边框呈现脊状,像是相册的厚相框一样.
        '''
        
        self.label03.pack()
        
if __name__=="__main__":
    root=Tk()
    root.geometry("960x540+300+200")
    root.title("标题文字")
    app=Application(master=root)
    root.mainloop()