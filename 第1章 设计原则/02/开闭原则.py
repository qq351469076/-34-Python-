class Icar:

    def __init__(self, name_, price_):
        # 车名
        self.name = name_
        # 车价格
        self.price = price_

    # 获取车名
    def getname(self):
        return self.name

    # 获取车价格
    def getprice(self):
        return self.price


class BenzCar(Icar):
    pass


class Shop4S:

    def __init__(self):
        self.carList = []

    def run(self):
        self.carList.append(BenzCar("梅赛德斯-迈巴赫S级轿车", 138))
        self.carList.append(BenzCar("梅赛德斯-AMG S 63 L 4MATIC+", 230))
        self.carList.append(BenzCar("梅赛德斯-奔驰V级", 50))

        self.carList.append(FinanceBenzCar("梅赛德斯-迈巴赫S级轿车", 138))
        self.carList.append(FinanceBenzCar("梅赛德斯-AMG S 63 L 4MATIC+", 230))
        self.carList.append(FinanceBenzCar("梅赛德斯-奔驰V级", 50))

        for car in self.carList:
            print("车名：" + str(car.getname()) + "\t价格：" + str(car.getprice()) + "万元")


class FinanceBenzCar(BenzCar):

    def getprice(self):

        if 50 <= self.price <= 100:
            self.price += self.price * 0.02
        elif self.price > 100:
            self.price += self.price * 0.05
        return self.price


if __name__ == '__main__':
    # 开闭原则是设计模式中的总原则，开闭原则就是说：对拓展开放、对修改关闭。
    shop4s = Shop4S()
    shop4s.run()
    # 开闭原则要求我们尽可能通过拓展来实现变化，尽可能少地改变已有模块，特别是底层模块。
    # 开闭原则总结:
    #   提高代码复用性
    #   提高代码的可维护性
