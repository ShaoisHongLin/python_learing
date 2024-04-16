# 方括号[]提取字符串的对应位置,最左为0  最右为-1或者借助len()-1

a='abcde'
print(a[0])
print(a[-1])
print(a[len(a)-1])  # 借助len()-1