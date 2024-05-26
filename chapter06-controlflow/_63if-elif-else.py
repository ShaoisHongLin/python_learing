# if-elif-else多分支选择

# 多分支选择elif写其它情况，else是都不满足的结果
# 另外，else可写可不写，顺序不可更改
'''
if 条件1:
	语句块1
elif 条件2:
	语句块2
elif 条件3:
	语句块3
[else:
	都不满足时候的结果]  #中括号表示可以不写else也可以写else
'''


# 常用于实际生活中划分范围
#(0-60分)(60-80分)(80-100分)

score=int(input("请输入一个学生的得分"))
if score<60:
	grade=("没及格")
elif 60<=score<80:
	grade=("60-80分")
elif 80<=score<100:
	grade=("80-100分")
else:
	grade=("请输入0-100的数字")

print("分数是{0},结果是{1}".format(score,grade))