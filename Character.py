class Character:
    def __init__(self, name=None):
        self.HP = 100
        self.ATK = 10
        self.HEAL = 20
        self.name = name

    def attack(self, object):
        if self.HP > 0:
            object.HP -= self.ATK
        else:
            print("攻撃を与えられません")
        if object.HP <= 0:
            object.HP = -1

    def heal(self, object):
        if object.HP < 100:
            object.HP += self.HEAL
        if object.HP >= 100:
            object.HP = 100


class Player(Character):
    def __init__(self, name):
        super().__init__(name)
        self.ATK = 10
        self.HEAL = 20


class Enemy(Character):
    def __init__(self, name):
        super().__init__(name)
        self.HP = 50
