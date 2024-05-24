# python常用字符串函数2：
# strip  首尾裁剪函数,叫做"裁剪"，但是理解为对数据的"清理"更好。


'''
实际开发中，经常会获取到
1.用户输入的字符串
或者
2.从文件中拿到的字符串数据

但往往，数据中可能有回车，空格，或者开头结尾写了些的特殊字符，这些字符如果不做预处理可能会造成代码处理不符合预期效果。
'''

# 如下示例，用户输入的姓名字符串左右不小心按了几下空格。对于这种信息要正确处理。

user_input = "   Alice   "
cleaned_input = user_input.strip()
print(cleaned_input)  # 输出 'Alice'


# 如下示例：具体的裁剪可分为两侧，左l  右r。

a='^a^^b^^c2^'
print(a.strip('^'))   #strip去除最左侧或者最右侧出现的，一个或者连续的这个内容，不会去除中间的。
print(a.lstrip('^'))   #只对最左边裁剪
print(a.rstrip('^'))   #只对最右边裁剪
a='    ^a^^b^^c2^    '
print(a.strip())     # 不写内容，则表示去除左右两侧的空格



# 后面还会学习对于文件的读取写入操作，也涉及文件的换行以及首位的字符问题

with open('example.txt', 'r') as file:
    lines = [line.strip() for line in file]
print(lines)  # 假设文件中每行都清理了末尾的换行符
