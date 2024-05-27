# lambda，(蓝博哒，带bd俩字母)匿名函数，声明一个没有名字的函数，它也是函数的定义方式，
# 仅用一行就能生成函数对象，需要用变量接收，它是最短的函数，只能有一个表达式，放在冒号后，且表达式就是返回其返回值。

f=lambda arg1,arg2,arg3:arg1+arg2+arg3

print(f)# 直接输出函数对象，会显示其对象类型信息。<function <lambda> at 0x0000028056A78A40>

print(f(1,2,3))


g=[lambda arg1:arg1,lambda arg2:arg2,lambda arg3:arg3]
print(g)
print(g[0](6),g[1](6),g[2](6))# 这里的g[0]、g[1]、g[2]是函数对象，理应可以访问