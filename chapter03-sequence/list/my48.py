# 讲解对list内元素的删除
# 对元素的删除、底层仍旧是后面的元素拷贝到前面一位。

# del a[2] 注：del放在前面，不是a.del。
'''
del对列表对应索引该位置后续的所有内容拷贝到前一个位置，达到删除效果。
del a[2]，使用即可，无返回值。
'''
a=list(['a','b','B','c','d','e'])
del a[2]
print(a)