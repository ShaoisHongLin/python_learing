'''
当在python中定义函数时,常常设定函数需要参数列表,并调用时候传递真实的参数。本节要了解函数的"参数传递方式":
'''


'''
1.先了解为什么要理解函数"参数"的"传递方式",懂了又有什么用?
'''
# 答：理解参数传递的方式，
    #1.主要是为了更好地去决定"用，还是不用return语句"，有什么影响。
    #2.现象：函数的作用域是局部的，但有时发现函数执行完外部传入的对象并没有受到影响，但有时又发现函数对外部对象又造成了实际影响。


# 在实参传递给形参的过程中---------python采用的是哪种传递方式？
    # 1.是类似C++里面，实参是作为对象的实体传进函数内部(值传递)?

    # 2.还是说python是以"内存引用"的方式，将参数传进函数内(按对象引用传递)？


    # 答：python的"参数传递"，使用"按对象引用传递"参数,传递的是"参数对象的引用"（或者内存地址），但这种行为的实际情况会根据"参数对象的类型",呈现两种不同的形式。
'''
            以下是对于参数对象的两种类型的分类情况:
'''

            # 1.如果传进来的参数对象是不可变对象：
'''
                如str、int、tuple,
                "函数体内的处理逻辑的它”和“实际传进来之前的参数”,它们在共享着同一个地址，
                由于所作用的对象类型是不可变的，《创建出来一个同类型的新的对象，使得新的对象受到改变》，原对象"暂时在函数体内"被替换成了同名的新对象,
                只要不在return里返回该新对象的值,函数执行前后的结果就是,不可变对象值不会受到影响。
'''
            # 2.如果传进来的参数对象是可变对象:
'''
                如list、dict,就算是不写return,函数执行时回也会对其造成影响:
                 "函数体内的处理逻辑的它”和“实际传进来之前的参数”,它们在共享着同一个地址，
                 在修改时,《并未产生新的对象,直接指向同一个对象,直接引用它进行修改》,产生影响。

                 (当参数对象是可变对象时候的知识尤为重要,往往要搭配下一章节讲的"深、浅拷贝"一起使用，"深、浅拷贝"知识，是为了增强数据的封装性，使函数体内的操作
                 不影响原始数据)
'''
            # 再细致点讲：python的参数"对象的引用传递"，更通俗叫做"按共享传递"（pass-by-sharing），实参并不传递给实参实际的对象，而是实际对象的引用，"函数体内的它”和“实际传进来之前的参数”,它们在共享着同一个地址。

'''
        def modify(x):
            x = 5
            

        a = 10
        print(modify(a))   # 输出 10(例子中是int是不可变类型,因此属于参数的引用传递规则,对于"不可变类型"的一种,参数对象"未受到影响"。)




        def modify(lst):
            lst.append(5)
            

        my_list=[1,2]
        print(modify(my_list))   # 输出[1,2,5](例子中是lsit是可变类型,因此属于参数的引用传递规则,对于"可变类型"的一种,参数对象"受到影响"。)


'''

'''

1.以下这部分可以作为不可变类型的示例,体会"过程中是否有新对象的产生",用于更好地理解python的参数传递方式。
def modify_immutable(x):
    print("ID inside function (before modification):", id(x))
    x = x + 1  # 尝试修改x
    print("ID inside function (after modification):", id(x))
    return x

# 创建一个整数对象
a = 10
print("ID outside function (original):", id(a))
# 调用函数
new_a = modify_immutable(a)
print("ID outside function (after function call):", id(a))
print("ID of new object returned by function:", id(new_a))

'''



'''

2.以下这部分可以作为可变类型的示例,体会"过程中没有新对象的产生",用于更好地理解python的参数传递方式。
def modify_mutable(lst):
    print("ID inside function (before modification):", id(lst))
    lst.append(3)  # 修改列表
    print("ID inside function (after modification):", id(lst))
    return lst

# 创建一个列表对象
my_list = [1, 2]
print("ID outside function (original):", id(my_list))
# 调用函数
new_list = modify_mutable(my_list)
print("ID outside function (after function call):", id(my_list))
print("ID of returned object by function:", id(new_list))

'''