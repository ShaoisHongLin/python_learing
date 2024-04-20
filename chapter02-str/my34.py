# python常用字符串方法2：
# strip  首尾裁剪函数
a='^a^^b^^c2^'
print(a.strip('^'))   #strip去除最左侧或者最右侧出现的，一个或者连续的这个内容，不会去除中间的。
print(a.lstrip('^'))   #只对最左边裁剪
print(a.rstrip('^'))   #只对最右边裁剪
a='    ^a^^b^^c2^    '
print(a.strip())     # 不写内容，则表示去除左右两侧的空格