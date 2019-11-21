# 工厂类
class Factory:

    def new_television(self):
        pass

    def new_refrigerator(self):
        pass


# 电视类
class Television:

    def do_something(self):
        pass


# 冰箱类
class Refrigerator:

    def do_something(self):
        pass


# TCL电视
class TCLTelevision(Television):

    def do_something(self):
        print('我是TCL电视机, 我可以看电视')


# 美的电视
class MeiDTelevision(Television):

    def do_something(self):
        print('我是美的电视机, 我可以看电视')


# TCL冰箱
class TCLRefrigerator(Refrigerator):

    def do_something(self):
        print('我是TCL冰箱, 我可以放东西')


# 美的冰箱
class MeiDRefrigerator(Refrigerator):

    def do_something(self):
        print('我是美的冰箱, 我可以放东西')


# TCL工厂
class TCLFactory(Factory):

    def new_television(self):
        return TCLTelevision()

    def new_refrigerator(self):
        return TCLRefrigerator()


# 美的工厂
class MeiDFactory(Factory):

    def new_television(self):
        return MeiDTelevision()

    def new_refrigerator(self):
        return MeiDTelevision()


def main():
    factory = TCLFactory()

    television = factory.new_television()
    refrigerator = factory.new_refrigerator()

    television.do_something()
    refrigerator.do_something()

    # ===========我是分割线======================

    factory = MeiDFactory()

    television = factory.new_television()
    refrigerator = factory.new_refrigerator()

    television.do_something()
    refrigerator.do_something()


if __name__ == '__main__':
    main()
