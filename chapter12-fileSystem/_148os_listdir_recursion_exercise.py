# 这节用最近学过的os.listdir()和前面学习的递归函数进行一个小练习,找到一个目录并输出目录下的所有文件的路径,并用缩进划分出层次,打印出目录树的原始结构。

'''
这节主要的作用是回顾简单的递归算法的设计和os和os.path的混合使用。
'''

import os

def list_files(path):
    # path="f:\\test2_recursion_print"
    list=os.listdir(path)    
    for item in list:
    #['subdir1', 'subdir2', 'file4.txt']
        full_path=os.path.join(path,item)
        if os.path.isdir(full_path):
            # 如果是目录
            print("目录"+full_path)
            list_files(full_path)
        else:
            # 如果是文件
            print("     "+"文件"+full_path)

if __name__=="__main__":
    list_files("f:\\test2_recursion_print")