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





'''
异常名称                说明
ArithmeticError     所有数值计算错误的基类
AssertionError      断言语句失败
AttributeError      对象没有这个属性
BaseException       所有异常的基类
DeprecationWarning  关于被弃用的特征的警告
EnvironmentError    操作系统错误的基类
EOFError            没有内建输入,到达EOF 标记
Exception           常规错误的基类
FloatingPointError  浮点计算错误
FutureWarning       关于构造将来语义会有改变的警告
GeneratorExit       生成器(generator)发生异常来通知退出
ImportError         导入模块/对象失败
IndentationError    缩进错误
IndexError          序列中没有此索引(index)
IOError             输入/输出操作失败
KeyboardInterrupt   用户中断执行(通常是输入^C)
KeyError            映射中没有这个键
LookupError         无效数据查询的基类
MemoryError         内存溢出错误(对于Python 解释器不是致命的)
NameError           未声明/初始化对象 (没有属性)
NotImplementedError 尚未实现的方法
OSError             操作系统错误
OverflowError       数值运算超出最大限制
OverflowWarning     旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning 关于特性将会被废弃的警告
ReferenceError弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError        一般的运行时错误
RuntimeWarning      可疑的运行时行为(runtime behavior)的警告
StandardError       有的内建标准异常的基类
StopIteration       迭代器没有更多的值
SyntaxError         Python 语法错误
SyntaxWarning       可疑的语法的警告
SystemError         一般的解释器系统错误
SystemExit          解释器请求退出
TabErrorTab          和空格混用
TypeError           对类型无效的操作
UnboundLocalError   问未初始化的本地变量
UnicodeDecodeErrorUnicode 解码时的错误
UnicodeEncodeErrorUnicode 编码时错误
UnicodeErrorUnicode 相关的错误
UnicodeTranslateError Unicode 转换时错误
UserWarning         用户代码生成的警告
ValueError          传入无效的参数
Warning             警告的基类
WindowsError        系统调用失败
ZeroDivisionError   除(或取模)零 (所有数据类型)
'''