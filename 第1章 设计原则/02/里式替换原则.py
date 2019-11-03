class AbstractAnimal:

    def __init__(self, name_):
        self.name = name_

    def dance(self):
        print(self.name + '开始跳舞')


class Rabbit(AbstractAnimal):
    pass


class Person:

    def __init__(self):
        self.animal = None

    def feedanimal(self, animal_object):
        self.animal = animal_object

    def walkanimal(self):
        print('人开始溜动物')
        self.animal.dance()


if __name__ == '__main__':
    # 里氏替换原则的解释是，所有引用基类的地方必须能透明地使用其子类的对象。
    # 只要父类能出现的地方子类就可以出现, 并且使用子类替代父类, 不会产生任何错误或异常, 使用者可能根本就不需要知道是父类还是子类
    person = Person()
    person.feedanimal(Rabbit('小白兔'))
    person.walkanimal()
    # 里氏替换原则是开闭原则的基础, 它告诉我们设计程序的时候尽可能使用基类进行对象的定义及引用, 具体运行时在决定基类对应的具体子类型

    # 里式替换原则总结
    #   里式替换可以提高代码复用性, 子类继承父类时自然继承到了父类的属性和方法
    #   提高代码可拓展性, 子类通过实现父类方法进行功能拓展, 个性化定制
    #   里式替换中的继承有侵入性, 继承, 就必然拥有父类的属性和方法
    #   增加了代码的耦合性, 父类方法或属性的变更, 需要考虑子类所引发的变更
