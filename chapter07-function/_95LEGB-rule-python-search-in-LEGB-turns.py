# python搜寻一个名称时候，遵循LEGB规则


'''
在开始搜寻一个名称开始的位置起,直到找到这个名称。

假如它位于的是嵌套函数内部。
它就会先对于本嵌套函数nested function(这里代表了local)
再去它的外围enclose函数搜寻
再去更外部的Global看
最后再看python自己定好的名称们。 

'''
# 1.Local，先从函数的内部的方法里面找
# 2.Enclosed，再从嵌套的函数里面的外围函数找
# 3.Global，全局变量
# 4.Built-in类型，python自己写好的名称

# 示例代码:
s="global"

def outer():
    s="outer"
    
    def inner():
        s="innner"
        print(s)

    inner()

outer()

# 解释代码：这里的print(s)，就涉及到了s名称的搜寻工作，python中按照LEGB，它先搜寻它所在的local部分，直接就找到了s。

# 如果此代码处没找到，它将继续搜寻enclosed的部分：outer()

# 如果仍没找到，会去搜寻更外面的Global的s

# 最终的最终还是找不到，会去python内置的几个关键类型查一圈，多半是找不到。

# 本段代码很简单，对于s名称的搜寻工作，刚开始就在local范围找到了。