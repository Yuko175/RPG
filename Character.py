class Character:
    def __init__(self, name=None):
        self.HP = 100
        self.ATK = 10
        self.HEAL = 20
        self.name = name

    def attack(self, object):
        if self.HP > 0:
            object.HP -= self.ATK

    def heal(self, object):
        if self.HP < 100:
            object.HP += self.HEAL
        else:
            print("HPが満タンです")
        if self.HP >= 100:
            object.HP = 100
            print("HPが満タンです")


class Player(Character):
    def __init__(self, name):
        super().__init__(name)


class Enemy(Character):
    def __init__(self, name):
        super().__init__(name)
        self.HP = 100
