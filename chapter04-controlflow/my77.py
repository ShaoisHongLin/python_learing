# 字典推导式：

# 语法：{key_expression:value_expression for item in 可迭代对象}

# 字典推导式往往会使用zip来处理可迭代对象部分
# 第一部分：定义key和value以及相应的改动，
# 第二部分：item选择你要引用的对象
# 第三部分：可迭代对象里面用zip(迭代对象1、迭代对象2...)
values=["sam","tom","amy","bob","simon"]
a={id*100:value for id,value in zip(range(1,6),values)}
print(a)



# 常用知识：利用字典推导式，可以得知一个文章中各个不同字符出现的次数。
'''
平常我们对文本进行操作的方式，往往是将一个文章直接读取成一个巨长的字符串存入一个变量里面。
my_text='a b c d e F g Hello World ddddddddd   oo ooo  aa'

利用字典的推导式，我们就可以对于一个长文本变量进行遍历示例：in my_text。
char_count={letter: my_text.count(letter) for letter in my_text}
print(char_count)
'''
my_text='a b c d e F g Hello World ddddddddd   oo ooo  aa'
char_count={letter: my_text.count(letter) for letter in my_text}
print(char_count)

# 这个功能如果放在其它语言里面，会写很多行，但是python利用好推导式，就可以很快写出来。