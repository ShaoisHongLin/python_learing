# shutil模块。   

# 我们之前可能见过util，英文是utility，意思是效用，有用性，实用的设施、工具。 因此在java中util类被常常叫做工具类。
# 我们之前可能也学过shell，shell是操作系统之间沟通的内核，我们所有的指令在最后交给操作系统之前都是先变为shell。

# shutil 就是shell 和util的结合，该模块是提供了一个辅助工具的模块，达到类似shell效果，比如：处理文件和目录的复制、移动、删除、压缩和解压缩等操作。


# 如果我们学过linux的相关内容之后才来学习python,可以把这个模块当作类比linux的基本命令的操作集合。
'''
常用的操作

(一)shutil的拷贝操作:

拷贝单个文件
shutil.copyfile("src","dest")


拷贝目录涵盖的多个文件
shutil.copytree("src",  "dest" ,ignore=shutil.ignore_patterns("*.html","*.htm")   )
这是一个深度拷贝的操作,其中你可以在最后添加ignore的参数,来识别需要忽略的文件模式,用通配符模糊匹配。这里选择忽略.html,和.htm文件,进行拷贝时候遇到它们则会忽略。
'''
import shutil

shutil.copyfile("f:\\123.txt","f:\\copy_123.txt")

shutil.copytree("f:\\test1","f:\\test_shutil_copytree",ignore=shutil.ignore_patterns("*.py"))
# 这个在拷贝目录的时候将会忽略指定的内容。

'''
(二)shutil的压缩归档操作:   


make_archive(base_archive_path,format,base_path)这是对单个文件夹的归档压缩,不是挑拣多个文件后构成压缩包。
重要的必填参数是三个,分别是压缩后的名字,归档格式,文件路径

解释：|archaiv|读音,意思是档案,或者归档的操作,计算机中类似于压缩操作,就叫做archive.
'''


shutil.make_archive("f:\\zip_test1","zip","f:\\test1")
