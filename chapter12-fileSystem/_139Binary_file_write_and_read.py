# 了解了如何读写普通文本文件之后,学习如何读写二进制文件，比如图片。

'''
其实读写二进制文件几乎和普通文件的读写是一样的,只不过模式要加上"b"(binary)来表示二进制的"读rb/写wb/追加ab"模式
'''


# 这里对于二进制文件就要用到遍历line的方式而不是直接f.(write或者read)lines的操作了。
# 这里对动漫里面路飞图片进行一个拷贝。srcFile是对于源文件source的取名，destFile是对目标生成文件destination的取名。
with open(r"G:\图片\luffy.jpg","rb")as srcFile,open("G:\图片\copy_luffy.jpg","wb")as destFile:
    for line in srcFile:
        destFile.write(line)