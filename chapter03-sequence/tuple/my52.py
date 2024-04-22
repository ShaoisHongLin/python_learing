# 利用zip合并list1、2、3为tuple
# zip(list1，list2,list3)  ：利用多个列表合成一个元组。
'''
对应位置拼在一起，如果长度不均，按最短的那个为止。
'''
a=[1,2,3,4]
b=["a","b","c","d"]
c=["A","B","C","D","E"]
d=zip(a,b,c)
print(d)   #<zip object at 0x0000024B50BF8540> 生成的是一个zip对象，需要转化为list()
# 转化为list对象
e=list(d)
print(e)