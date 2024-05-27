# 1.可变位置参数*param,称为 "位置参数 打包" 或 "可变 位置参数"(可变二字表示的是，实参的参数数量可以不确定)


# 2.可变关键位置参数**param，称之"可变关键字位置参数"，默认是dict的"关键字+值"的形式


# 3.强制命名参数(*param,a,b)把*param放在括号内第一个，调用时候需要在实参处以命名参数每个都填好。

# 示例：可变位置参数示例：
def print_values(a, b, c, *args):
    print(a, b, c, *args)

print("------------------------------------------")
print_values(1, 2, 3, 'four', 'five')



# 示例:可变关键字位置参数：
def print_values(a, b, c, **kwargs):
    print(a, b, c)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_values(1, 2, 3, name='Sam', age=18)

'''
可变参数后面加多少个参数，都会被塞进*元组、**字典里。
'''

# 示例：强制命名参数

def print_values(*arg,a,b,c):
        print(*arg,a,b,c)

print_values(0,a=1,b=2,c=3)
