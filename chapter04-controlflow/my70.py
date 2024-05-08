# 如果循环是对于现实数据中的表格进行查找打印

# 1.区别在于遍历的对象由自己x是定义的range，变为table(dict对象)内的row1、row2...(list对象)

# 2.如果用if筛选的话，使用成员函数.

r1={"name":"tom","age":18,"score":66}
r2={"name":"sam","age":18,"score":77}
r3={"name":"amy","age":20,"score":88}
tb=[r1,r2,r3]

for x in tb:
	if x.get("score")>70:
		print(x)