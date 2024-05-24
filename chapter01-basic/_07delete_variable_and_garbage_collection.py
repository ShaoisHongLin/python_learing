# 上节课学了"创建"变量并初始化，这节学del"删除"变量,与闲置对象的垃圾回收机制

a=3
del a
print(a)

# 如 del a ，即可删除不再使用的变量.

'''
闲置的对象会被当垃圾回收。
上一节讲到变量赋值流程：产生heap中的对象----绑定其地址给变量，
如果del删除变量，此时heap对象的值没有对象名绑定在一起，会被闲置，于是触发python中闲置对象的垃圾回收机制，不再占用内存。
'''