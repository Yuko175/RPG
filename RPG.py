from Character import *
import random

# 私たちが選べる要素
# 防御力
# ロールづくりー魔法使い、剣士


def main():
    character_list: list = []
    main_player_name = input("名前を入力してください：")
    set_main_player_name(character_list, main_player_name)
    set_sub_player_name(character_list)
    set_enemy_name(character_list)

    print(battle(character_list, main_player_name))


def set_main_player_name(character_list, main_player_name):
    player = Player(main_player_name)
    character_list.append(player)


def set_sub_player_name(character_list):
    player2 = Player("Bob")
    character_list.append(player2)


def set_enemy_name(character_list):
    for i in range(3):
        enemy = Enemy(f"Slime_{i}")
        character_list.append(enemy)


def battle(character_list, main_player_name):
    while is_battle_continue(character_list):
        action_list = random.sample(character_list, len(character_list))
        for character in action_list:
            for object in action_list:
                if character == main_player_name:
                    print("敵に攻撃しますか？それともHPを回復させますか？")
                    print("攻撃なら「1」を回復なら「2」を入力してください")
                    main_player_move = input("あなたの行動を教えてください：")
                    pass
                elif character.__class__.__name__ != object.__class__.__name__:
                    character.attack(object)
                    print(f"{character.name}は{object.name}に攻撃した")
                    break
            print("--------------")
            for character in character_list:
                print(f"{character.name}:{character.HP}")
            print("--------------\n")
            if is_battle_continue(character_list) == False:
                return "終わり"


def is_battle_continue(character_list):
    for character in character_list:
        if character.HP <= 0:
            return False
    return True


if __name__ == "__main__":
    main()
