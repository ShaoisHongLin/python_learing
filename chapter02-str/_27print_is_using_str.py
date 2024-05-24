# str()与print暗含的str()处理
# 1.简单易懂，str()可以将其它类型转化为字符串
a=1
b=2
print(str(a)+str(b))

# 2.print其实解释器调用了str()来将非字符串对象转化成为了字符串。