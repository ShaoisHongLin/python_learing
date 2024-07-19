# 包:package包,必须是里面带有一个__init__.py名称的,才能叫做包。---------__init__的起名是固定格式，一个包必须有它。

# 包的用途:将功能类似的模块放在同一个包内.


'''
(一)、正确地使用from import来减轻代码的长度问题

包package的内部也是存在着嵌套的关系,假如包和包之间嵌套着,我们导入一个内部的模块之后,调用时就会发现会代码十分冗长。

而前面学习的from import刚好是为了解决包名前缀太长导致代码的冗长的问题.

import a.aa.aab.aaba.xxx()
调用:
a.aa.aab.aaba.xxx()


from a.aa.aab.aaba import xxx()
调用:
xxx()
'''


'''
(二)__init__.py文件在包中的作用


    我们导入一个包的时候import a
    实质上是导入了包里面的__init__.py,将它执行一次,而不是导入包里面的各个py文件(模块),而是视__init__.py里面的导入内容而定。

在__init__.py文件中,需要做的是对于各个py文件(模块)进行批量导入.
'''

'''
# __init__.py的示例

import month_salary
import year_salary
import average_salary
import total_salary

if __name__=="main":
    print("导入了month_salary包")
    print("导入了year_salary包")
    print("导入了average_salary包")
    print("导入了total_salary包")
    
    
# 这样一来,我们导入一个包,实质上就是执行一i此包中的__init__.py这个文件,将里面涉及的模块批量导入.
'''



'''
(三)、了解即可:from a import *模糊导入包内全部模块.(很不推荐在生产环境中使用,)

我们前面提及了为什么建议from xx import 具体模块,而不要使用通配符*来进行全部导入:
    因为大的项目时候导入了多余的包很有可能导致其中一个的模块的方法调用起到了冲突,调用同名的错误来源的方法.造成未知错误而且难以debug出来。


但是我们还是了解一下这个操作的原理: 
在__init__.py文件里面事先定义一个"__all__这个变量",赋值进去一个列表,列表里的每个元素会在from a import *的操作时候导入.
比如:


# __init__.py文件

__all__=["math","add","re"]


这样就可以配合from a import *使用了,尽管不推荐这么写,会在导入项过多时候造成未知的同名冲突,以及导入时候的效率低下。
'''