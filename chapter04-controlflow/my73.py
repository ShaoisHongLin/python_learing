# 循环while和for的“else”

teamnumber=0
salarys=[]
for x in range(3):
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
else:
    print("else的部分会在此处，正常地循环结束运行了")
print("员工数",teamnumber)
print("工资列表",salarys)