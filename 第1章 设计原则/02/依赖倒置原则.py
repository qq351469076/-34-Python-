class Shop:

    def __init__(self, name_):
        self.name = name_

    def sell(self):
        return f'在{self.name}购物'


class WanDaShop(Shop):
    pass


class Customer:

    def __init__(self, name_):
        self.name = name_

    def shopping(self, shop):
        print(f'{self.name}{shop.sell()}')


if __name__ == '__main__':
    # 依赖倒置原则的定义：程序要依赖于抽象接口，不要依赖于具体实现。简单的说就是要求对抽象进行编程，不要对实现进行编程
    # 这样就降低了客户与实现模块间的耦合。
    # 核心思想是: 要面向接口编程, 不要面向实现编程
    wanda = WanDaShop('万达')
    zhangsan = Customer('张三')
    zhangsan.shopping(wanda)
    # 依赖倒置原则总结
    #   高层模块不应该依赖底层模块, 都应该依赖抽象(接口或抽象类)
    #   接口或抽象类不应该依赖于实现类
    #   实现类应该依赖于接口或抽象类
