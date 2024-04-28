# 字典元素的键值对增添、修改

# 1.a["键"]=值
'''
键已存在会在对应处覆盖，不存在则在末尾增添。
'''
a=dict(name="shao",age=18,score=90)
a["age"]=19
a["height"]='180cm'
print(a)

# 2.a.update()参考一个dict对另一个dict做更新，重复的会覆盖
a=dict(name="shao",age=18,score=90)
b=dict(name="shao",age=18,score=90,height="185cm",weight="65kg")
a.update(b)
print(a)