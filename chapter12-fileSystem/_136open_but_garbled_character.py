# 我们使用filesystem的最常用的操作就算open文件的操作


# Garbled character problem:字符乱码问题：

# open操作,会有一个字符集编码的问题,对于ASCII码，以及完全继承ASCII码的UNICODE里的字符都不会产生乱码问题。

# 中文字符并不在UNICODE里面，而是在UNICODE的UNICODE TRANSFORMATION FORMAT，也就是UTF里面，是对于UNICODE的一种转换形式。

# 我们应该采用UTF-8来避免乱码问题，这是很简单的。











'''
另外,还专门总结了一个关于字符集编码的总结图片,在本目录的_136的.png文件
'''