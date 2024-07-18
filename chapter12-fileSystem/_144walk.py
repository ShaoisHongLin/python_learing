# os模块的walk是用于递归遍历目录树的,它可以重点讲解一下,尽管不能熟练使用，但是后续可以回看.

'''
os.walk()是目录文件的遍历器.

(一):
os.walk()的语法：
    os.walk(top, topdown=True, onerror=None, followlinks=False)
    top,英语意思大致为“最高层”,----是要遍历的"根目录"
    topdown模式:意思是先把最高层的目录遍历一遍,再遍历它们里面涵盖的子目录。而不是遇到有子目录时就立刻遍历里面的内容。
    followlinks模式:意思是将可识别linux上的软连接,不再默认地将软连接视作文件而是前往软连接并也遍历里面的内容。

os.walk的返回值需要重点讲解,是三元的元组,(root,dirs,files),目录路径,包含的目录,包含的文件.
    其中root路径是字符串,而dirs和files都是列表形式。它们都作为可遍历对象,因此后续很好地去操作。
我们用一个变量接收这个三元元组。
'''

# 示例:
import os

path="F:\\test1"
file_list=os.walk(path,topdown=True)
for root,dirs,files in file_list:
    for x in dirs:
        print(os.path.join(root,x))
    for x in files:
        print(os.path.join(root,x))

'''
至于topdown的模式可以切换true和false来体会一下。
'''