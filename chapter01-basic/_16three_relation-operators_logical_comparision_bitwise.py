# 关系运算符：1.逻辑运算符and、 or、 not
'''
'与运算符':and
'或运算符':or
'非运算符':not
'''
# 逻辑运算符存在：”逻辑短路“


e = 100 > 200 and 50 < (3 / 0)
print(e)
# 逻辑短路：左侧满足了整个逻辑，就完全不再对右侧做判断。
# 如：and，一旦出现左侧逻辑判断是"FALSE"，便不会理会右侧。(只要代码能编译通过运行，右侧的值完全不会进行计算或进行判断，即使你右边拿0做除数,过了编译就不会报错)




# 关系运算符：2.比较运算符

    # 注：python中关系运算符可以连用.

    d,e,f=1,2,3
    if(d<e<f):                           # 这种"连续的"比大小，在C语言里是没有的。
        print('连续的关系运算符')

# 关系运算符：3.位运算符  & | ^  << >>

# 问？什么是位运算？



# 是很陌生的概念。与十进制的直接比较不同，位运算是发生在二进制内部的，& | ^  （与、或、异)，先将二进制数字左侧零填充后，对每一位作比较，
# 三者的用法是:& | ^  这三者，分别满足"与、或、异"则该位为1，否则为0


a = 11
b = 22
print(bin(a))
print(bin(b))

# bin()可以转化十进制为二进制。
'''
二进制的数字比较过程中，(0b右侧：二进制的标识)，左边填0以补齐二者的位数。
11：0b 1011
22：0b 10110

那么在比较前会变成
11：0b 01011
22：0b 10110
'''
print(bin(a & b))  # 按位与运算：两个都为1则=1
# 0b 00010
print(bin(a | b))  # 按位或运算：两个中其中有1则=1
# 0b 11111
print(bin(a ^ b))  # 按位异或运算：两个不同则=1
# 0b 11101


print(a << 2)  # 全体位数左移两位。整体相当于乘4

print(b >> 1)  # 全体位数向右移1位，整体相当于除2

