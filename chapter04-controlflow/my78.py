# 集合set的推导式,也和dict一样使用花括号，语法是"列表的推导式"类似的格式。

# 语法：接近列表版
# {表达式 for item in 可迭代对象}或者带if的判断版{ 表达式 for item in 可迭代对象 if 条件判断}

a={x for x in range(1,100) if x%9==0}
print(a)
print(type(a))
# 集合内是无顺序的，可以回忆一下，可以发现如果x%9那么多半会乱排布，x%2可能会按人性化顺序排布。