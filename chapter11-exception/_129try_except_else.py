try:
    a=input("请输入被除数的值")
    b=input("请输入除数的值")
    c=int(a)/int(b)
except BaseException as e:
    print(e)
else:
    print("已经正确输出,未遇到异常",c)

# 如果遇到异常则执行except下面的内容，没有遇到异常则会执行else的内容
    
