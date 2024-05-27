# 对于嵌套函数我们已经了解了，它分为"外围函数"和"内层函数"。

# 我们这节介绍只有在嵌套函数结构出现，只能在内层函数声明的一种变量，nonlocal。


# 解释澄清：

'''
nonlocal并不是针对整个文件,成为global变量,它只是在嵌套情景下,放在内层函数内，对外围函数的变量进行操作。

因此,在外围函数中也必须有这个变量跟内层函数的nonlocal的部分对应。


使用nonlocal的作用:内层函数的nonlocal的值修改,会反映到外层函数的作用域中。

注:nonlocal完全不要联系起global的知识点,nonlocal不是global的全局变量,只是用于嵌套函数的"内、外之间"操作数据的场景。
'''

# 代码示例：

def outer():
    a=555555

    def inner():
        nonlocal a
        a=66666
        print('outer内的a在inner被nonlocal的a修改了,且影响到了外围函数的a值')

    inner()
    print(a)

outer()