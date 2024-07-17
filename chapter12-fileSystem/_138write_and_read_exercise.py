# 假设文件里面有几行文字，做个小练习，在每行行末增加  #和"行号"。

# 步骤分析：
# 1.先读取，读取后在身体里面进行相关逻辑操作。
# 2.再写入。

with open(r"f:\123.txt","r",encoding="utf-8") as f:
    lines=f.readlines()  
    #['哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈\n', '哎我擦\n', '啊啊啊']
    #lines_new=[ line+"#"+str(index) for index,line in zip(range(1,len(lines)+1),lines)]


    lines_new=[ line.rstrip()+"     #"+str(index)+"\n" for index,line in zip(range(1,len(lines)+1),lines)]
    print(lines)
    print(lines_new)
    '''
    其中,最复杂的一行是怎么写出来的呢？
    
    1.首先,我们同时遍历两个遍历,也就是并行遍历。
    for index,line in zip(1位置 2位置)

    2.然后index需要从实际的索引中遍历---"数组索引"的range范围---,line需要从实际的lines中遍历。
    for index,line in zip( range(1,len(lines),lines)  填写好"位置1"和"位置2"

    3.然后利用被遍历的对象进行遍历时的操作,最后赋值给变量。
     [ line+"#"+str(index) for index,line in zip(range(1,len(lines)+1),lines)]
    '''

    '''
    发现写出之后还是不完美
    最后加符号加在了换行符后面怎么办?

    对line对象右侧去除line右侧原有的"\n"在想要的格式产生之后，最后再补上"\n"
    lines_new=[ line.rstrip()+"#"+str(index)+"\n" for index,line in zip(range(1,len(lines)+1),lines)]
    '''

    
with open(r"f:\123.txt","w",encoding="utf-8") as f:
    s=lines_new
    f.writelines(s)

