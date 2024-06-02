# 工厂设计模式如何向单例版的工厂设计模式转变。

'''
class Posche:pass
class Benchi:pass
class Byd:pass


class CarFactory:
    def createCarInstance(self,brand):
        self.brand=brand
        if brand=='保时捷':
            return Posche()
        if brand=='奔驰':
            return Benchi()
        if brand=='比亚迪':
            return Byd()
        else:
            return"品牌未知,无法生产"

factory=CarFactory
c1=factory().createCarInstance("保时捷")
print(c1)
'''

class Posche:pass
class Benchi:pass
class Byd:pass


class CarFactory:
    _instance=None
    _init_flag = True  # 初始化标志
    def __new__(cls,*args,**kwargs):
        if cls._instance==None:
            cls._instance=super(CarFactory,cls).__new__(cls,*args,**kwargs)
        return cls._instance
    
    def __init__(self):
        '''
        这个init其实是可以省略的,以及上面设定的初始化标识_init_flag = True也是可以省略的,
        但是如果像这样写出init的部分,又可以在此方法内增加一些伴随初始化一起执行的功能,
        比如下面这行print()进行简单的打印提示。
        '''
        if CarFactory._init_flag:  
            # 意思是只要走过一次init，就将init的flag设置为false，使得下一次
            #再调用 __init__ 方法时，由于 _init_flag 已经是 False，因此不会再次执行初始化代码。
            print("实例对象初次产生了")
            CarFactory._init_flag = False

    def createCarInstance(self,brand):
        self.brand=brand
        if brand=='保时捷':
            return Posche()
        if brand=='奔驰':
            return Benchi()
        if brand=='比亚迪':
            return Byd()
        else:
            return"品牌未知,无法生产"

factory1=CarFactory()
print(factory1)
factory2=CarFactory()
print(factory2)

'''
<__main__.CarFactory object at 0x000002737EE7B950>
<__main__.CarFactory object at 0x000002737EE7B950>
这里由于编写成singleton的模板形式,因此第二个实例化对象不会产生,仍会是最初创建的那个对象。
且仅在创建第一个对象的此刻消耗资源(因为该单例模式),之后就会一直驻存在存储中,生命周期随整个app结束才会结束。
'''