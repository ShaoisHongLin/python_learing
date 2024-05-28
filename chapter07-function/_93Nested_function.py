# python支持在函数里面嵌套函数，即在函数里面定义另一个函数。通常把他们叫"外围函数(enclosing function)"和"内层函数(nested function)"。


#  被定义在内部的函数不能在外界被调用，只能在定义它的函数中调用,以下是基本示例：


def outer():
    print("调用了外部的函数")
    def inner():
        print("调用了内部的函数")
    
    
    inner()

outer()
# inner()则在外界无法调用。

'''
这种内部嵌套定义的函数,有什么具体的使用场景呢？
'''
# 1.目的性：降低重复度高的代码部分，将它们整合。

'''
        可以使得重复度高的函数被整合,用逻辑来执行各自的函数,降低代码中大量重复的而相似的部分。

            def printChineseName(lastname,familyname):
                print('{0}{1}'.format(lastname,familyname))

            def printAmericanName(lastname,familyname):
                print('{0}{1}'.format(familyname,lastname))

            这两处代码重复度极高,只是改了一个打印顺序位置,逻辑重复度极高的这一行就可以被提取出来塞到更里面一层,让外层决定调用的格式。

            def outer_print_name(country,lastname,familyname):
                # 下面两行,先对内部函数进行定义,具体怎么使用再添加外层的逻辑.
            def inner_print(param1,param2):
                print('{0}{1}'.format(param1,param2))

        
            if country=="China":
                inner_print(param1,param2)

            else:
                inner_print(param2,param1)
'''

'''
2.封装,完全禁止内层函数(nested function)被外界访问:

def outer():
    print("调用了外部的函数")
    def inner():
        print("调用了内部的函数")
    
    
        
inner()
'''
# 对2：封装并完全禁止访问的解释：在enclosed function更外面的外部,就根本无法调用内部的nested function


'''
3.闭包(后面看会再回来看就懂了)

    -----闭包是编程中的一种概念和做法。

    -----目的是:实现功能的"隐藏且封装"


    具体做法:
        1.在外围函数中,内部的嵌套函数通过nonlocal影响了外围函数.
        2.外围函数需要return嵌套函数的对象,这样嵌套函数就成功'闭包'了。
        3.这一部分可以单独放到一个函数名内,单独拿出来调用,这就是闭包。
        
    它的功能就算闭包可提供给更外界了,而且具有隐藏性。
'''
# 代码示例：闭包简单示例：闭包的关键在于外围函数return内层函数的对象名。
    

#    def outer(x):
#        y = 5
#    def inner(z):
#        return x + y + z
#    return inner

    # 创建一个闭包
#closure = outer(10)
    # 调用闭包
#print(closure(2))  # 输出 17