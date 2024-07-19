# 当我们需要动态导入的时候,python有专门的动态导入模块importlib,这个模块提供了各种动态导入的功能,支持动态导入的操作

'''
(一)动态导入？

就是用一个变量,接收别人传进来的变量对应的模块名.
对于importlib模块中最基础的就是动态导入了.
    <1>创建字符串对象
    <2>使用importlib的特定方法并返回一个importlib对象 
'''
import importlib

s="math"
a=importlib.import_module(s)
print(a.sqrt(81))
# 输出9.0


'''
(二)重新加载模块

对于import 同一个模块,只会第一次被加载,只会执行一次。
但是如果我们真的有重新导入的需求,可以使用importlib模块的reload()
'''

importlib.reload(s)
# 在有需求的情况下,重新导入一次这个模块