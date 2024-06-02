# 设计模式:(一)工厂模式

# 工厂模式,实现了调用者和实现者的分离.   设置了专门的工厂类,工厂类负责"《类的实例化》或者说《创建对象》",工厂类在里面进行逻辑判断,统一决定实例化哪个类


'''
工厂模式对于多个并列的类能够进行有效的逻辑处理选择什么情况实例化哪个类。
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