class Sender:

    def send(self):
        pass


class EmailSender(Sender):

    def send(self):
        print('发送邮件')


class SmsSender(Sender):

    def send(self):
        print('发送短信')


class ExpressSender(Sender):

    def send(self):
        print('发送快递')


class SendFactory:
    """
    工厂类
    """

    @staticmethod
    def produce(type_):

        if not type_:
            return None
        elif type_ == 'email':
            return EmailSender()
        elif type_ == 'sms':
            return SmsSender()
        elif type_ == 'express':
            return ExpressSender()
        else:
            return None


def main():
    sendfactory = SendFactory()

    sendersms = sendfactory.produce("sms")
    sendersms.send()

    senderemal = sendfactory.produce("email")
    senderemal.send()

    senderexpress = sendfactory.produce("express")
    senderexpress.send()


if __name__ == '__main__':
    # 一个模型, 用来大规模生产同类的产品, 该模式将对象的具体实例过程抽象化, 并不关心具体的创建过程
    # 简单工厂模式: 一个工厂类根据传入的参数, 动态决定应该创建哪一类产品类(这些产品类均继承自一个父类的接口)实例
    # 这里引入两个角色, 一个是类的设计者, 一个是类的使用者, 类的使用者只关心"这个对象做这些事"
    # 而不关心"这件事如何去做", 通常, 类的设计者才会去关心"如何去做"
    # 优点
    #   1. 一个调用者想创建某个对象, 只需知道其名称即可
    #   2. 屏蔽具体行为实现, 调用者只需关心产品接口, 减轻调用者负担
    #   3. 拓展性高, 如果想增加一个产品类, 只需拓展一个工厂类即可
    main()
