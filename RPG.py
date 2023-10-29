from Character import *
import random

# 私たちが選べる要素
# 防御力
# ロールづくりー魔法使い、剣士


def main():
    character_list: list = []
    player = Player("Alice")
    player2 = Player("Bob")
    character_list.append(player)
    character_list.append(player2)

    for i in range(3):
        enemy = Enemy(f"Slime_{i}")
        character_list.append(enemy)

    # 敵と戦う
    while is_battle_continue(character_list):
        action_list = random.sample(character_list, len(character_list))
        for character in action_list:
            for object in action_list:
                if character.__class__.__name__ != object.__class__.__name__:
                    print(f"{character.name}は{object.name}に攻撃した")
                    character.attack(object)
                    break
            print("--------------")
            for character in character_list:
                print(f"{character.name}:{character.HP}")
            print("--------------\n")


def is_battle_continue(character_list):
    for character in character_list:
        if character.HP <= 0:
            return False
    return True


if __name__ == "__main__":
    main()
