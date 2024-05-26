# continue通常用来处理，“小错误建议重新来过”的部分。

# 这段代码的例子是对一个列表进行持续输入，直到有q的指令退出。
teamnumber=0
salarys=[]
while True:
    salary = input("请按顺序输入员工薪资")
    if salary.upper() == "Q":
        print("检测到Q的输入，退出了循环")
        break
    if float(salary)<0:
        print("输入了小于0的薪资，重新输入")
        continue
    print("未检测到错误，录入了一条数据")
    teamnumber+=1
    salarys.append(float(salary))
print("员工数",teamnumber)
print("工资列表",salarys)