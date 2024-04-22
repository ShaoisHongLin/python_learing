# python列表的按值重新排序

# 1.sort() 默认进行按值升序排序
a=list([8,9,4,5,7,6])
a.sort()
print(a)  # 可以看到升序排序了。
# 2.sort(reverse=True) 添加reverse参数=True进行倒序排序
a.sort(reverse=True)
print(a)

'''
可以被reverse替代：
a.reverse()
print(a)
'''
a.reverse()
print(a,'reverse()可以单独使用，和sort里面增加reverse参数作用一致')

# 3.利用random模块和shuffle()打乱顺序
import random
random.shuffle(a) # 进行“shuffle”翻译过来是洗牌，即随机打乱操作，每次都会变。
print(a)

# 4.sorted 将更改的（升序）排序放入新列表内。
a=list([8,9,4,5,7,6])
b=sorted(a)
print(b,"sorted普通版")

# 5.sort(a,reverse=True)  将更改的（升序）排序放入新列表内。
a=list([8,9,4,5,7,6])
b=sorted(a,reverse=True)
print(b,"sorted带reverse版")

'''
进行一个小总结。上面讲了sort()和sorted()，以及带reverse版本的二者，它们是有区别的。
如：
sort()类似英语的主动语态形式。改动直接影响原列表本身，也就是函数内有return更改了实际的值。
sorted()类似英语的被动语态形式。改动结果用变量接收的返回值呈现。
'''


# 6.简单讲解了reversed返回迭代器的用法
"""
上面提到过reverse()单拎出来是与sort(reverse=True)是一致的效果，
 但是被动版的b=reversed()的使用就稍有不同了，
 它跟前面sorted被动版(接收值是一个列表)不同，reversed() (其接收值是一个list的迭代器)
 
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

# 7.max 和min和sum
a=[1,2,3,4,5]
print(max(a))
print(min(a))
print(sum(a))