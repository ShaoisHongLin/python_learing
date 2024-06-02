# 单例对象Singleton Pattern     

# 单例对象模式,保证了该类只会产生一个对象。

# 适用场景:对象的创键消耗资源较大，比如创建某个对象时候需要读取各种配置文件的资源、以及过程中产生很多对象，依赖它们来创建本对象，
# 这种对象并提供全局的访问接口，以在各个地方使用,并且永久驻存在内存中,以免多次再创建消耗较大资源。

'''
配置管理：游戏客户端通常有一个全局的配置管理器，用于读取和存储配置参数。这些配置参数在客户端运行过程中可能会被多次读取，因此使用单例模式来确保配置管理器的唯一实例，可以避免重复读取和初始化配置数据。

资源管理：游戏客户端需要加载大量的资源，如图像、声音、模型等。资源管理器可以使用单例模式来确保只有一个实例，统一管理资源的加载、缓存和释放，避免重复加载相同资源，提高资源利用效率。

日志记录器：一个全局的日志记录器实例可以通过单例模式实现，用于记录客户端的各种运行信息、错误和调试信息，方便开发和维护。

网络管理：网络连接和通信通常也是通过单例模式管理的，确保客户端与服务器之间的通信是通过唯一的网络管理器进行，统一处理网络请求和响应。

'''



class ConfigManager:
    _instance = None
    #这是一个保护(protected)类型的instance类属性,在此处用于保存类的唯一实例。初始值为None,表示还没有创建实例
    # 此属性的设置是为了改写__new__需要的返回值和用于判断的一个属性,从而实现instance自创建以来数量一直保持唯一对象且对象是最开始创建的一个.
    def __new__(cls, *args, **kwargs):

    # __new__的作用是在类被实例化的第一步，new是__init__即将被调用的前一刻运行的,__new__是负责创建实例的,而__init__是用来负责初始化实例对象的。
    #  __new__的主要逻辑是"创建instance实例并return它"
    # 一般是直接写：instance = super("子类自身", cls).__new__(cls)
       if cls._instance is None:    
        #这里也可以写成 if not cls._instance:表示实例为空时候.abs
        # 加if是为了检测目前该类是否拥有过 实例，控制实例个数为1且实例对象一直是第一次创建的那个实例.
        # 第一次s1=Student()时候显然是符合if =None，创建出第一个instance.abs
        # 第二次s2=Student()时候，检测到出现过instance，在单例模式中，那么就返回上一次的instance而不产生第二个
            cls._instance = super(ConfigManager, cls).__new__(cls, *args, **kwargs)
            '''
            理解 super() 的参数
                super(当前类, cls):

                    1.这里 super() 第一个参数是当前类，即正在定义的类。
                    2.第二个参数是类对象 cls,这绝大多数的使用场景都是用于__new__方法的重写,因为他属于类方法
                
                super(当前类, self):

                    1.这里 super() 的第一个参数是当前类，即正在定义的类。
                    2.第二个参数是实例对象 self,因为包括__init__和其它方法,通常用于实例方法。

            其实这里的super(本类.cls).__new__
            就和找到他的父亲object,object().__new__是一个含义。
            '''
            cls._instance._load_config()
            return cls._instance

    def _load_config(self):
        # 假设这里加载配置文件内容
        self.config = {"resolution": "1920x1080", "volume": 75}

    def get_config(self, key):
        return self.config.get(key)

# 使用示例
config1 = ConfigManager()
config2 = ConfigManager()

print(config1.get_config("resolution"))  # 输出 '1920x1080'
print(config1 is config2)  # 输出 True,说明 config1 和 config2 是同一个实例
