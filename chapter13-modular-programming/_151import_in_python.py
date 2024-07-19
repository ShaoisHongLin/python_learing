# import
# 或者import ... as 别名   

'''
这是import进行"模块"的导入,python中导入的过程其实是调用了__import__()函数,并生成了type为<class 'module'>“模块”类型的对象.

''' 

import math as m

print(id(m))
print(type(m))   # <class 'module'>

'''
(一)别名----as
我们使用别名可以提高模块在实际代码编写时候的打字效率。

比如:
import math as a
改名前math.sqrt()
改名后m.sqrt()
'''

'''
(二)from 模块 import 成员

从一个模块中只导入某个成员,这样可以只挑选我们需要的模块的部分内容导入,从而让代码打字过程中也更为有效率。

比如:
from math import sqrt
仅导入成员前:print(math.sqrt(81))
仅导入成员后:print(sqrt(81))

无论是别名还是from,都可以一定程度上提到写代码时候的书写效率。
'''

'''
不要去做的操作
from xxx import *
我们还是建议不要写*,因为大的项目时候导入了多余的包很有可能导致其中一个的模块的方法调用起到了冲突,调用同名的错误来源的方法.造成未知错误而且难以debug出来。

我们最好还是from xxx import 具体的模块
'''