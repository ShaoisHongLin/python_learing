# 本节介绍常见的exception

'''
1.Synax Error  语法参数错误       

单词synax |sin-tax的读音|是句子的结构的意思,grammatical arrangement of a sentence



2.Name Error  标识符没有被声明

单词name在编程中,代之的不是"名字",而是指标识符,也就是变量或者说函数名的引用问题。
常常的出现格式是:NameError: name 'x' is not defined


3.Type Error 类型(还没开始赋值前)错误

往往在操作符的其中一个orphand,也就是"操作数"出现了错误。
比如:123+'abc'  TypeError:unsupported operand type(s) for +: 'int' and 'str'


4.Attribute Error类型: 属性错误,访问不存在的属性

比如：
a=100
a.f1()  int object has no attribute f1


5.Index Error 索引越界异常

6.KeyError  找不到对应的键


熟悉未知的、更多的异常情况,是为了将未知的错误祛除不敢尝试的情绪克服,沉下心来分析每一个异常。
'''