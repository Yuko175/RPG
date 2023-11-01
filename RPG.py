from Character import *
import random

# 私たちが選べる要素
# 防御力
# ロールづくりー魔法使い、剣士


def main():
    character_list: list = []
    player_list: list = []
    enemy_list: list = []
    main_player_name = input("名前を入力してください：")
    set_main_player_name(character_list, player_list, main_player_name)
    set_sub_player_name(character_list, player_list)
    set_enemy_name(character_list, enemy_list)

    print(battle(character_list, player_list, enemy_list))


def set_main_player_name(character_list, player_list, main_player_name):
    player = Player(main_player_name)
    character_list.append(player)
    player_list.append(player)


def set_sub_player_name(character_list, player_list):
    player2 = Player("Bob")
    character_list.append(player2)
    player_list.append(player2)


def set_enemy_name(character_list, enemy_list):
    for i in range(3):
        enemy = Enemy(f"Slime_{i}")
        character_list.append(enemy)
        enemy_list.append(enemy)


def battle(character_list, player_list, enemy_list):
    while is_battle_continue(player_list, enemy_list):
        action_list = random.sample(character_list, len(character_list))
        for character in action_list:
            if character.HP > 0:
                for object in action_list:
                    if object.HP > 0:
                        if character.__class__.__name__ != object.__class__.__name__:
                            # TODO:変える↓character_list[0]
                            if character == character_list[0]:
                                print("敵に攻撃しますか？それともHPを回復させますか？")
                                print("攻撃なら「1」を回復なら「2」を入力してください")
                                main_player_move = input("あなたの行動を教えてください：")
                                if main_player_move == "1":
                                    character.attack(object)
                                    print(f"{character.name}は{object.name}に攻撃した")
                                    if object.HP <= 0:
                                        enemy_list.remove(object)
                                    break
                                if main_player_move == "2":
                                    for heal_player in player_list:
                                        character.heal(heal_player)
                                    print(f"{character.name}と仲間のHPが回復した")
                                    break
                            # TODO:変える↓character_list[1]
                            elif character == character_list[1]:
                                character.attack(object)
                                print(f"{character.name}は{object.name}に攻撃した")
                                if object.HP <= 0:
                                    enemy_list.remove(object)
                                break
                            else:
                                character.attack(object)
                                print(f"{character.name}は{object.name}に攻撃した")
                                if object.HP <= 0:
                                    player_list.remove(object)
                                break
                    else:
                        break
                print("--------------")
                for character in character_list:
                    print(f"{character.name}:{character.HP}")
                print("--------------\n")
                if is_battle_continue(player_list, enemy_list) == False:
                    if player_list == []:
                        return "敵の勝ち！プレーヤーの負け"
                    if enemy_list == []:
                        return "プレーヤーの勝ち！敵の負け"


def is_battle_continue(player_list, enemy_list):
    if player_list == [] or enemy_list == []:
        return False
    return True


if __name__ == "__main__":
    main()
