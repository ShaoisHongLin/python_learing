# 上节我们介绍可以利用shutil模块，进行类似shell的一些简单功能，利用shutil.archive可以用于归档文件夹为zip

# 这节我们介绍一个专门用于压缩和解压缩的模块------zipfile

'''
zipfile模块:

(一)写入文件到压缩文件
zipfile_ZipFile("path","w")这是先创建一个zip的文件对象,我们挑拣多个文件后写入这个zip文件对象。
其中第一个参数是以.zip为后缀的具体路径,w是写入,代表创建zip文件对象并写入。

write(path1)
write(path2)
write(path3)
write(path4)
close()


(二)提取文件从压缩文件
zipfile_ZipFile("path","r")这是先创建一个zip的文件对象,从其中读取文件。
extractall("path")解压缩到哪个目录
'''

import zipfile

zip_object=zipfile.ZipFile("f:\\a.zip","w")
zip_object.write("f:\\123.txt")
zip_object.write("f:\\123456.txt")
zip_object.write("f:\\a.txt")
zip_object.close()


zip_object=zipfile.ZipFile("f:\\a.zip","r")
zip_object.extractall("f:\\zip_extract_result")
zip_object.close()