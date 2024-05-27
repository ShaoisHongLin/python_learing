# 参数传递中，不可变对象里还有tuple，tuple里面如果设置可变变量呢，底层是怎样的,如a=(1,2,[5,6])


# 结论：当对于不可变对象tuple里面修改可变对象，会影响到函数外部的对象。
a=(1,2,[5,6])

def test(b):
    print("前",id(b))
    a[2][1]=7
    print(a)
    print("后",id(b))

print(id(a))
test(a)