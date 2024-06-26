# 递归算法：自己调用自己，为了不让自己落入死循环，会设终止条件，比如if...return一个值，return作为终止。

# 递归算法中，会调用生成大量的对象
# 在栈中，函数运行时候，第一次循环开始开启一个栈帧，执行到"调用自己的语句"则再次开启一个栈帧...一直套娃，
# 直到终止之后，从最终不再套娃的那个开始回推，一个个消亡。

# 如果不是为了使用特定情况的算法，不要使用递归程序。


'''
递归设计一个阶层运算6!=6*5*4*3*2*1
'''

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(6))

'''

怎么样思考.并给出递归的算法的代码呢？

6!为例子
最外层:6*5
下一次:5*4
下一次:4*3
下一次:3*2
最后一词:2*1


递归算法
1.先自己列出大致的规律,
2.逐步"拆解"
3.只要找到"拆解的关键"--------"哪个位置应该进行递归操作"。就接近于写出了这部分代码。

'''