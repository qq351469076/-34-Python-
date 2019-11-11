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
    def produce_sms():
        return SmsSender()

    @staticmethod
    def produce_email():
        return EmailSender()

    @staticmethod
    def produce_express():
        return ExpressSender()


def main():
    sender_email = SendFactory.produce_email()
    sender_email.send()

    sender_sms = SendFactory.produce_sms()
    sender_sms.send()

    sender_express = SendFactory.produce_express()
    sender_express.send()


if __name__ == '__main__':
    # 多方法简单工厂在前者的基础上改进来的, 普通工厂方法在使用时, 如果type类型传递错误则不能正确创建对象
    # 多方法直接将produce中的逻辑展开到具体的方法中, 从而避免该问题
    # 一般我们会将"多方法"设置为静态的, 从而避免类的频繁实例化, 拿来即用
    main()
