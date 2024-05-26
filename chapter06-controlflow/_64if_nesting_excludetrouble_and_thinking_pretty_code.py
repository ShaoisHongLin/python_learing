# if else if用缩进嵌套。以及用条件匹配情况的两种思路。

'''
if的嵌套可以用来写"排除掉错误情况："


注：缩进很重要在python里
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



# 2.减少不必要的if嵌套，可以用if直接优化处理。

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
degree='ABCDE'                    # 先囊括所有的选项
score=int(input("请输入分数"))       
num=0
num=score//10
if num<6:
    num=5
print("分数是{0}，等级是{1}".format(score,degree[9-num]))
'''
