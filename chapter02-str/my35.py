# python常用字符串方法3：
# 大小写相关函数
a='abcdefghijklmnopqrstuvwxyz'
print(a.capitalize())   # 整个字符串首字母大写
a='i love python'
print(a.title())        # 每个隔开的单词首字母大写
print(a.upper())        # 全变为大写
a='HELLO PYTHON'
print(a.lower())      #全变成小写
a='big SMALL'
print(a.swapcase())      # 全变为相反的大小写