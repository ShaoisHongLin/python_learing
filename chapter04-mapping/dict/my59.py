# 对现实中的'表'，用dict转化为dict(每一行)和list(各行)

'''
r起名为row'行'的缩写
r1=dict(name="shao",age=18,score=85)
r2=dict(name="shi",age=19,score=85)
r3=dict(name="qin",age=19,score=87)

tb起名为table'表'的缩写
tb=list([r1,r2,r3])
'''
r1=dict(name="shao",age=18,score=85)
r2=dict(name="shi",age=19,score=85)
r3=dict(name="qin",age=19,score=87)

tb=list([r1,r2,r3])

# print(tb)  dict是可以直接打印出来的
print(tb)
# 想获取表的第一条记录的age项。
a=tb[0].get("age")
print(a)

# 将每一行的name项打印
for i in range(len(tb)):
    b=tb[i].get("name")
    print(b)

# 将整个表按表的结构打印出来
for i in range(len(tb)):
    print(tb[i].get("name"),tb[i].get("age"),tb[i].get("score"))