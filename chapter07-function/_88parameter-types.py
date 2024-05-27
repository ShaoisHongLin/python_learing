# python的参数类型：位置参数，默认值参数，命名参数

def test1(a,b,c):
    print(a,b,c)
    
test1(1,2,3)
# 位置参数必须一 一对应，不能缺少。

def test2(a,b,c=2,d=3):
    print(a,b,c,d)
test2(1,2)
# 默认值参数，顺序从头开始，提供足够参数即可。
# 注：默认参数必须放到其它参数的后面

def test3(a,b,c):
    print(a,b,c)
    
test3(b=1,c=2,a=3)
# 命名参数，顺序无所谓。