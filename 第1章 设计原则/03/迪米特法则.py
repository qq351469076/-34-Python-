class Teacher:

    @staticmethod
    def command(leader_):
        print(f'女生的总数为{str(leader_.countgirls())}')


class Girl:
    pass


class GroupLeader:

    def __init__(self, girl_list):
        self.list = girl_list

    def countgirls(self):
        return len(self.list)


if __name__ == '__main__':
    # 迪米特法则, 有时候也叫作最少知识原则, 它的定义是: 一个软件实体应当尽可能少地与其他实体发生相互作用
    # 迪米特法则初衷在于降低类之间的耦合

    # 在通俗来讲:
    #   如果两个类不必彼此直接通信，那么这两个类就不应当发生直接的相互作用。
    #   如果其中的一个类需要调用另一个类的某一个方法的话，可以通过第三者转发这个调用。
    teacher = Teacher()
    leader = GroupLeader([Girl(), Girl()])
    teacher.command(leader)
