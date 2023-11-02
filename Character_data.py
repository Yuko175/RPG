class Character:
    def __init__(self, name=None):
        self.HP = 100
        self.ATK = 10
        self.HEAL = 20
        self.name = name

    def attack(self, target):
        if self.HP > 0:
            target.HP -= self.ATK
        if target.HP <= 0:
            target.HP = -1

    def heal(self, target):
        if target.HP < 100:
            target.HP += self.HEAL
        if target.HP >= 100:
            target.HP = 100


class Player(Character):
    def __init__(self, name):
        super().__init__(name)
        self.ATK = 10
        self.HEAL = 20


class Enemy(Character):
    def __init__(self, name):
        super().__init__(name)
        self.HP = 50
