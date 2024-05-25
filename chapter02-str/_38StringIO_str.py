#StringIO对象

# python自带的字符串是不可以改变的，只能以重新将此变量与另一个对象的绑定，它不是纯正意义上的改变值，str终究是基本数据类型，不可改变。


# 但是python其实提供了一种可变字符串，它用于处理，数据流中的字符串，它将该字符串容纳进"缓冲区"。

# 将字符串变为StringIO对象之后，该对象是放在字符串缓冲区，通俗的把这个字符串整体看作一个文件即可。

# StringIO对象内是真正的可变字符串，我们可以调用StringIO对象的一个方法，来将它看作一个字符串的文件来进行模拟操作，而不需要真的建立一个文件收录这些字符串。

import io

str="abcd1234"

str_io=io.StringIO(str)      #将str转化为可变字符串


# 注意，由于该对象是以缓冲区形式存在，它的内置操作都是以指针的方式在内存中操作的，因此比如.seek(3),那么实质上我们将StringIO对象在该字符串的指针移动到对应的第三个索引位置。

# 1.StringIO，不能被直接print查看，只能通过StringIO对象特有的函数.getvalue()
print(str_io.getvalue())

# 2.StringIO如何修改一处地方
# 使用StringIO对象内特有的.seek(里面填字符串的索引位置，而不是值),再进行写入write()

str_io.seek(2)

str_io.write("***")
print(str_io.getvalue())
