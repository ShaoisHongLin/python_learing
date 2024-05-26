# 选择语句的流程控制语法：(双分支)

# 1.if-else语句
'''
if 条件1:
	语句块1
else:
	语句块2
'''

a=input("请输入一个数字")
if int(a)<10:
	print(a)
else:
	print("该数字>=10")

# 2.讲解一下简单的双分支赋值情况下，一个三元运算符和if-else是可以互换的。

	# <<------------满足则向左取，否则向右取
	# 条件为真时候的值 if (条件表达式) else 条件为假时候的值
'''
num if (a<10) else("数字太大")
'''

num=int(input("请输入一个数字"))
b=num if (num<10) else("数字太大")
print(b)