# 生成器:(是生成器，元组对应的是生成器表达式，而不是推导式)


# 语法：(表达式 for item in range 可迭代对象 if )，重点是小括号。

tuple1=(x for x in range(1,10) if x>5)
print(tuple1)# <generator object <genexpr> at 0x0000015A7DA6C380>
# 要用遍历取出生成器的内容,且仅可以遍历一次，因为生成器对象无法将其指针回归到头。
for x in tuple1:
    print(x)
# for x in tuple1:
#     print(x)  这次只能是空的
