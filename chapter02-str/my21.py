# python中字符串的创建
# 普通创建
a="abc"
print(a)
a='abc'
print(a)
# 涵盖""的字符串
b='my_name is "shao"'   #如果想在字符串里面写""则要用单引号放在最外面。

print(b)

b="my_name is \"shao\""  #不嫌麻烦，也可以使用转义字符 "my_name is \"shao\""，结果一样。
print(b)
# 多行字符串:保留预制化格式
s='''             
    i
      love
          python
    '''         #多行字符串
print(s)


#另外，python可以定义空字符串、len()函数查看字符串长度。
s=''
print(s)
print(len(s))