# eval函数，能够将字符串视为表达式。   该函数尤其不能在服务器使用，它可以被用于"注入攻击，比如里面被别人写删除相关的语句"

# 网络程序中字符串是可以传递的，另一台服务器，用eval()传递一个字符串给我们执行，删除操作。

a=1
b=2
c=eval("a+b")
print(c)