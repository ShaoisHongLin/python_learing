# 字典元素的键值对del(a[])删除、a.pop()弹出、a.clear()全部清除

a=dict(name="shao",age=18,score=90)
# 1.del(a[])删除
del(a["name"])  # del放在前面，并用[]访问该元素
print(a)
# 2.a.pop("key")弹出
b=a.pop("score")  # a.pop("key")
print(a)
print("弹出了",b,"的值")
# 3.a.clear()全部清除
a.clear()       # a.clear()全部清除
print(a)

# 4.popitem()随机弹出一组键值对，由于dict是无序列表，所以可以随机弹出。
a=dict(name="shao",age=18,score=90)
c=a.popitem()
print(c)