# 字典元素的键值对增添、修改

# 1.添加：直接访问赋值即可,如：a["name"]="sam"
'''
键已存在会在对应处覆盖，不存在则在末尾增添。
'''
a={"id":"1","score":90,"height":"175cm","sex":"male"}
a["age"]=19
a["height"]='180cm'
print(a)


# 2.修改：a.update(b),不是生成新对象，而是直接在原来对象上产生影响。
a=dict(name="shao",age=18,score=90)
b=dict(name="shao",age=18,score=90,height="185cm",weight="65kg")
a.update(b)
print(a)
