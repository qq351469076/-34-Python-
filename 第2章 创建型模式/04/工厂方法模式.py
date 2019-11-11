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


class Provider:

    def produce(self):
        pass


class ExpressSendFactory(Provider):
    def produce(self):
        return ExpressSender()


class EmailSendFactory(Provider):
    def produce(self):
        return EmailSender()


class SmsSendFactory(Provider):
    def produce(self):
        return SmsSender()


def main():
    provider_sms = SmsSendFactory()
    sender_sms = provider_sms.produce()
    sender_sms.send()

    provider_email = EmailSendFactory()
    sender_email = provider_email.produce()
    sender_email.send()

    provider_express = ExpressSendFactory()
    sender_express = provider_express.produce()
    sender_express.send()


if __name__ == '__main__':
    # 之前的简单工厂模式有个比较明显的弊端: 工厂类集中了所有实例的创建逻辑, 明显违背高内聚的责任分配原则, 违背了闭包规则
    # 工厂模式则是对该问题的进一步延伸解决, 差异就是将原先存在于一个工厂类中的逻辑抽调出来, 创建一个接口和多个工厂类,
    # 这样, 一旦功能有所增, 比如说我们要加一个"发送导弹"的功能, 只需要加一个"导弹发送工厂类", 该类实现produce接口返回
    # 实例化的"导弹发送类", 再在"导弹发送类"中, 实现具体的发送逻辑即可, 无需修改之前的业务代码, 拓展性比较好
    main()
    # 工厂方法模式中, 核心的工厂类(这里为Provider接口)不再负责所有产品的创建, 而是将具体创建的工作交给子类去做,
    # 该核心类仅扮演抽象工厂的角色, 负责给出具体工厂子类必须实现的接口, 而不接触哪一个产品类应该被实例化的细节,
    # 拓展性 较 简单工厂模式 提升明显
