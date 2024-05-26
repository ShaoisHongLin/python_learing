# function的return

'''
1.如果函数不写return,调用就会返回none值

2.问：如果想返回多个值怎么办？

    答。在写return之前,先用一个序列对象或者dict等对象将return的值提前存起来,返回那个对象即可。

    如:

    def printshape(n):
        s1="#"*n
        s2="$"*n
        return [s1,s2]

        
3.type(printshape)与type(printshape(3))哪个是函数的"返回值的类型",哪个是函数对象的类型.

type(printshape)是function类型,代表函数对象.type(printshape(3))是函数的"返回值的类型"
'''