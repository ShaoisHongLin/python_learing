# python常用字符串方法1：
# 查找和验证字符串
a='二十六个字母abcdefghijklmnopqrstuvwxyz二十六个字母'
len(a)
a.startswith('')   # 是否以`内容`开头
a.endswith('')   # 是否以`内容`结尾
a.find('')    # 查第一次出现
a.rfind('')   # 最后一次出现
a.count('')   # `内容`出现了几次
a.isalnum()   # 是否都是数字或字符is all num
