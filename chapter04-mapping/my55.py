# 字典的通过'键'访问

# 1.普通访问b=a["name"]，如果不存在，则抛出异常
a=dict(name="shao",age=18,score=90)
b=a["name"]
print(b)

# 2.a.get()访问，如果不存在，不会抛出异常，而是显示None，或者在括号内后面加缺省值。
a=dict(name="shao",age=18,score=90)
b=a.get("name")
print(b)
h=a.get("height")
print(h)
h=a.get("height","185cm")
print(h)

# 3.a.items()所有的键值对
print(a.items())  # dict_items([('name', 'shao'), ('age', 18), ('score', 90)])

# 4.a.keys()所有的键、a.values()所有的值
print(a.keys())  # dict_keys(['name', 'age', 'score'])
print(a.values())  # dict_values(['shao', 18, 90])

# 5.in键是否在字典中
print("name" in a)