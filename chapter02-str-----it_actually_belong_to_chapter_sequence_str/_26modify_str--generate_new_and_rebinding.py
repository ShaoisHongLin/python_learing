# 字符串的替换：replace()
'''
replace其实不是字面意思替代，而是参考一个对象产生新对象，然后由人为指向它。看起来像是替代了。
'''

'''
str前面提到，作为基本数据类型，是不可变序列，想完成对它的修改旧不能进入错误的思路：
错误思路：
a='abc'
a[1]=‘B’
print(a)
Error：'str' object does not support item assignment
‘item assignment’的行为表示‘对序列赋值’。但是str作为不可变序列，不支持这种操作。

正确思路，替换的本质不是修改，而是"如何获得一个新的对象"并指向新的对象。
如：
a='abc'
a='aBc'
print(a)
完成了'创建一个新的对象'，并用'原来的变量'指向了'新的对象',达成了视觉上的替代效果。
'''

# a.replace('old','new')
'''
a.replace，作用是参考旧的对象内容，生成新的对象内容。
新的对象内容由用户自己某个变量指向它来使用。
'''

a ='abc'
b=a.replace('b', 'B')
print(a)    # 旧的对象值仍旧没变，因为变量a仍旧指向原来的对象(a.replace()只是'产生'新的对象，不是更改对象)，
print(b)    # 新的变量b指向了由replace产生的新对象。

# 我们实际操作中看起来是将其不可变序列用replace修改了，其实是分了两步：
# 1.replace()产生新对象。
# 2.'正是原来的变量a'指向新对象。
a='abc'
a=a.replace('b','B')
print(a)   # 看起来被修改了。