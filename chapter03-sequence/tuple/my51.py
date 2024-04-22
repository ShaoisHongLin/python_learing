# 元组的访问、索引、计数、切片、生成排序的新元组

# 1.不能修改,因此不能赋值
# 2.a[2]访问、index()索引、count()计数、切片


a=tuple(["1","2","3","1"])

print(a[2])
print(a.index("1"))
print(a.count("1"))
print(a[1:3])


# 3.sorted产生排序后的新元组（list时候讲过）
b=sorted(a)
print(type(b))
print(b)