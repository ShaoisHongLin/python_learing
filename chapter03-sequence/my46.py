# python列表的遍历、复制

# 1.列表的遍历
a=list(['a','b','B','c','d','e'])

for temp in a:  # 遍历了列表的每个元素，可以在for内接操作
    print(temp)

'''
解释：
for “+随便取一个名字”   比如obj,temp,类似C++里面for行的i的作用，它是用于遍历的变量
'''

# 2.复制列表的所有元素到"新的"列表对象。
a=list(['a','b','B','c','d','e'])
print(id(a))
b=a+['f']  # 用加法或乘法实现新的列表对象。
print(id(b))
'''
错误示范：
a=list(['a','b','B','c','d','e'])
print(id(a))
b=a   # 这样做在python里，是将其新变量指向到旧对象，并未产生新的list对象。
print(id(b))
'''
a=list(['a','b','B','c','d','e'])
print(id(a))
b=a   # 这样做在python里，是将其新变量指向到旧对象，并未产生新的list对象。
print(id(b))