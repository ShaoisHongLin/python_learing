# if else if用缩进嵌套。以及用条件匹配情况的两种思路。
'''
1."缩进",在嵌套的if中很重要


# 比较简单的用法就是
if 排除掉错误情况：

else:
	if正确的几种情况
'''
score=int(input("请输入一个数字"))
if score<0 and score>100:
    print("请输入0-100的数字")
else:
	if score<60:
		grade=("没及格")
	elif 60<=score<80:
		grade=("60-80分")
	elif 80<=score<100:
		grade=("80-100分")

print("分数是{0},结果是{1}".format(score,grade))



# 2.感受用于匹配各种情况进行选择的两种思路：

# <1>
'''
第一种：全都分散开用if elif匹配
	if score<60:
		grade=("没及格")
	elif 60<=score<80:
		grade=("60-80分")
	elif 80<=score<100:
		grade=("80-100分")
'''

# <2>
'''
第二种:
degree='ABCDE'                    # 先囊括再所有的选项
score=int(input("请输入分数"))       
num=0
num=score//10
if num<6:num=5

print("分数是{0}，等级是{1}".format(score,degree[9-num]))
'''
degree='ABCDE'                    # 先囊括再所有的选项
score=int(input("请输入分数"))
num=0
num=score//10
if num<6:num=5

print("分数是{0}，等级是{1}".format(score,degree[9-num]))