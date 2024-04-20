#StringIO对象

# python自带的字符串是不可以改变的，只能新建对象来重新更改指向视觉上改变。
# 而io库有io.StringIO对象，是可变字符串。
import io
str="abcd1234"
str_io=io.StringIO(str)      #将str转化为可变字符串

# 1.StringIO，不能被直接print查看，只能通过.getvalue()
print(str_io.getvalue())

# 2.StringIO如何修改，要先.seek(索引)，再write("")

str_io.seek(2)
str_io.write("***")
print(str_io.getvalue())