# 迭代中使用zip() ----并行迭代for a,b,c in zip(names,ages,jobs):。
# for 遍历参数 in zip(被遍历的对象)    

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
# 这也是并行迭代，不是非得"使用zip()"
for i in range(min(len(names,ages,jobs))):
    print("{0},{1},{2}".format(names[i],ages[i],jobs[i]))




# 可以看一下后面_138里面的内容，再次提到并行迭代，就是用多个参数，对多个对象进行遍历。
# lines=f.readlines()  #最终lines是一个列表 ['哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈\n', '哎我擦\n', '啊啊啊']
# lines_new=[ line+"#"+str(index) for index,line in zip(range(1,len(lines)+1),lines)]

'''
第三行井号的那复杂的一行是怎么写出来的呢？
    
1.首先,我们同时遍历两个遍历,也就是并行遍历。
for index,line in zip(1位置 2位置)

2.然后index需要从实际的索引中遍历---"数组索引"的range范围---,line需要从实际的lines中遍历。
for index,line in zip( range(1,len(lines),lines)  填写好"位置1"和"位置2"

3.然后利用被遍历的对象进行遍历时的操作,最后赋值给变量。
[ line+"#"+str(index) for index,line in zip(range(1,len(lines)+1),lines)]
'''