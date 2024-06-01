# 类的多继承

# C++和python支持类的多继承，利用多继承可以让子类具有父类的特性

# 它的主要作用就是"集成多个功能"到一起，类似电视遥控器，手机控制中心等的目的。

'''
但多继承毕竟不同于单继承，它设定过多往往会导致"菱形问题"的产生,即上下最终都指向较少的对象,存在一个对象是是b的父亲的同时是c的父亲。

      A
     / \
    B   C
     \ /
      D
这种问题在python中以MRO机制得到了解决。python中都拥有最终的根类object,因此必须存在一种机制来解决菱形问题,

python采用了MRO机制,确保每个类在继承链中只会被访问一次,避免了重复调用和继承冲突,前面提到过一次,用mro()方法,查看类的继承关系,就是它的一种实用例子体现。
'''


'''
复杂性增加：多继承会增加代码的复杂性，特别是在理解和调试类,之间的关系时。
冲突：如果多个父类有同名的方法或属性，可能会导致冲突和意外行为。
维护困难：随着代码的增长，多继承的层次结构可能变得难以维护和扩展。
'''





# 示例 ：多继承实现一个类简单就能够"获取日志信息"，又能将"发送这个信息"，集成另外两个类的功能。
class Logger:
    def log(self, message):
        print(f"Log: {message}")

class Network:
    def send(self, data):
        print(f"Sending data: {data}")

class DataManager(Logger, Network):
    def process_data(self, data):
        self.log("Processing data")
        self.send(data)

# 创建DataManager的实例
manager = DataManager()
manager.process_data("Example data")


'''
    "多继承"可以采用"组合"的手段来代替

    组合强调“有一个”(has-a)的"拥有"关系,而不是继承所强调的(is-a)的“是”关系。

    "组合"具体的实现方式,就是通过先创建需要使用的类的实例,然后将实例对象传入到组合类里面,区别在于
    第1步.组合类需要先创建"想要的功能"的对象
    第2步.放在参数列表传进来,才能调用。

'''

'''
简单场景和独立功能：如果只是简单地将几个独立功能组合在一起，多继承可以快速实现。

复杂场景和灵活需求：如果需要更高的灵活性、更清晰的代码结构，以及更容易的维护，组合是更好的选择。


问：看起来,是否"多继承完全不如"组合"呢？

答：其实不然,

1.从调用方便程度来看：多继承由于是继承关系,它可以直接调用父类的方法,而不需要调用其父类相关功能的实例对象。实例对象不必产生即可调用其功能。
而组合则需要实例化想要使用的功能所在的类,然后再传递进来。


2.通过接口使用的方便程度来看:多继承的接口可以一口多用,可能叫做remote(空调遥控器)的接口里蕴含了多种功能,调用时候不需要记住内部具体的功能的类名(temperature,wind level,strong)。
调用可能是:remote.control("37度")
而组合在调用时候,除了接口还需要调用接口内具体的类名。比如想调用"温度条件"功能,就要写remote.control.temperature("37度")   的接口的具体功能。

但是,多继承关系绑定较为死板,维护想增加新功能的时候,需要重新改写那部分继承结构,而"组合"就只需要多加个参数进去。
'''



'''
class Logger:
    def log(self, message):
        print(f"Log: {message}")

class Network:
    def send(self, data):
        print(f"Sending data: {data}")

class DataManager:
    def __init__(self, logger, network):
        self.logger = logger
        self.network = network

    def process_data(self, data):
        self.logger.log("Processing data")
        self.network.send(data)

# 使用组合创建DataManager的实例
logger = Logger()------------------------------------------(这两行就是主要区别)
network = Network() ---------------------------------------(这两行就是主要区别)
manager = DataManager(logger, network)
manager.process_data("Example data")

'''


