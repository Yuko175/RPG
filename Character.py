class Character:
    def __init__(self, name=None):
        self.HP = 100
        self.ATK = 10
        self.name = name

    def attack(self, object):
        if self.HP > 0:
            object.HP -= self.ATK


class Player(Character):
    def __init__(self, name):
        super().__init__(name)


class Enemy(Character):
    def __init__(self, name):
        super().__init__(name)
        self.HP = 100
