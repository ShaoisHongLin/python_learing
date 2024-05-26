# 选择语句的流程控制语法：

# 1.选择：(单分支)

'''
if 语句:
	语句块
'''

# 最简单的两行使用
num=int(input("请输入一个数字"))
if num<10:
	print("它是小于10的整数，输入的是"+str(num))


# False、0、0.0、none、空序列对象、空range、空迭代器都=false

# 1.体会空序列为false
if 3:
	print("if 3会输出")

a=[]
if a:
	print("if 空序列不会输出")    # 空序列。

# 2.注意"False"非空字符串False算非空序列，不算False关键词。
if "False":
	print("'False'作为字符串"+"会输出")



# 3.回顾：条件判断里python可以使用连续的不等号如：0<a<10而不用0<a and a<10
a=5
if 0<a<10:
	print("条件里面可以使用连续的不等号")


# 4.注意：python跟C++等有条件判断处的区别：python不可以在条件处出现= ,等号字样。
a=10
# if a=10:   python不可以在条件处出现=