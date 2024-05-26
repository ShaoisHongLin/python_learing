# 介绍几个python中用于排序的列表函数。
# 在它们当中有的直接产生影响，直接影响本体
# 有的在函数内部生成新对象作为返回值，不会直接影响本体，用一个变量接收返回的新对象即可。



# 首先先来介绍3个直接作用于本体的，如:sort(),reverse(),random.shuffle()

    # 1.sort() 默认进行按值升序排序

    a=list([8,9,4,5,7,6])
    a.sort()
    print(a)  # 可以看到升序排序了。

    # 注：添加sort的参数，如:sort(reverse=True) 添加reverse参数=True,进行按大小的倒序排序

    a.sort(reverse=True)
    print(a)


    # 2.reverse() 不对值的大小、而是原本的顺序进行倒过来排序。
    a.reverse()
    print(a)
    

    # 3.利用random模块和shuffle()打乱顺序
    import random
    random.shuffle(a) 
    # 进行“shuffle”,shuffle 翻译过来是:"洗牌"，即"随机打乱"操作，每次运行shuffle都会变。
    print(a)


# 接着，介绍几个不直接影响本体，而是生成新的对象放到返回值来接收的函数。
# 1.sorted,将更改的（升序）排序生成新列表对象。

    a=list([8,9,4,5,7,6])
    b=sorted(a)
    print(b,"sorted普通版")

    # 注: b=sorted(a,reverse=True)  将更改的（降序）排序生成新列表对象。
    a=list([8,9,4,5,7,6])
    b=sorted(a,reverse=True)
    print(b,"sorted带reverse版")

'''
进行一个小总结，如果看懂上面内容可以跳过：

上面提到的是sort()和sorted(),它们是有区别的。

如：
sort(),长相类似英语的主动语态形式。
它的改动直接影响原列表本身，也就是函数内有return自身，更改了实际的值。

sorted(),类似英语的被动语态形式。函数内用返回值返回了新的对象，不在原值上产生影响
'''


# 上面不是还介绍了reverse()的主动，它有没有被动呢?
b=reversed(a)

"""
 它跟前面sorted被动版(返回生成一个新列表)不同，

 reversed() (返回的是一个list的迭代器)
 
 什么是迭代器？
 就是它不是是一个具体的对象，迭代器本身通过直接访问目标地址的方式来进行使用。
 
 a=[10,20,30]
 c=reversed(a)
 print(c) # <list_reverse iterator object at ...物理地址>

    如果接下来将迭代器c强制转化为list(c)那么它只能用于一次性操作，之后便不可使用。
    list(c)
    print(c)  # 第一次成功输出
    print(c)  # 第二次由于是迭代器转化而来，会输出空列表。
 """


a=list([10,20,30])
c=reversed(a)
print(c) # <list_reverse iterator object at ...物理地址>
print(list(c))  # 第一次成功输出
print(list(c))# 第二次由于是迭代器转化而来，会输出空列表。

#另外了解一下简单的查看最大、最小、总和的函数.max 和min和sum


a=[1,2,3,4,5]
print(max(a))
print(min(a))
print(sum(a))
