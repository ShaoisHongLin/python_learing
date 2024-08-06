# 这节讲简单的title和"定位"geometry

'''
window.title是弹窗的标题文字

window.geometry正如其字面意义,是几何的意思,是指尺寸和起始位置,之所以使用geometry是因为计算机图形学中将这种对于对象的形状尺寸位置叫做"几何"
具体使用:window.geometry("widthxheight+x_offset+y_offset")
如:window.geometry("960x540+300+200")
'''


from tkinter import *

window=Tk()
window.title("这里是自定义的弹窗的标题")
window.geometry("960x540+300+200")
window.mainloop()