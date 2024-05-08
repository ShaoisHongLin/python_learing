# 迭代中使用zip() ----并行迭代for a,b,c in zip(names,ages,jobs):。

'''
并行遍历就是在一般的迭代中，通过zip对多个序列对象，同时对它们的同一位置获取，在多个序列中最短的那个位置截止
'''

names=("tom","sam","amy","simon")
ages=(18,19,20)
jobs=("teacher","student","doctor","policeman")
for a,b,c in zip(names,ages,jobs):
    print("{0},{1},{2}".format(a,b,c))

'''
打印结果：
tom,18,teacher
sam,19,student
amy,20,doctor
'''

# 它和for i in rage 最后格式化时访问该序列names[i],ages[i],jobs[i]进行格式化输出结果一致。
# 这也是并行迭代，而不用非得使用zip()
for i in range(min(len(names,ages,jobs))):
    print("{0},{1},{2}".format(names[i],ages[i],jobs[i]))
