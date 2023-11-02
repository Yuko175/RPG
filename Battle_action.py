from Character_data import *
from Character_setup import *
from Battle_action import *
from Battle_other import *
import random


def battle(character_list, player_list, enemy_list, main_player_list, sub_player_list):
    turn_count = 0
    while is_battle_continue(player_list, enemy_list):
        turn_count += 1
        print(f"\n☆☆☆☆☆☆☆☆☆{turn_count}ターン☆☆☆☆☆☆☆☆☆\n")
        action_list = random.sample(character_list, len(character_list))
        for character in action_list:
            if character.HP <= 0:
                print(f"{character.name}のHPがなかったので攻撃できなかった！")
                result_print(character_list)
                continue
            for target in action_list:
                if target.HP <= 0:
                    continue
                if character.__class__.__name__ != target.__class__.__name__:
                    if character in main_player_list:
                        battle_main_player(
                            character, target, character_list, player_list, enemy_list
                        )
                        break
                    elif character in sub_player_list:
                        battle_sub_player(character, target, character_list, enemy_list)
                        break
                    elif character in enemy_list:
                        battle_enemy(character, target, character_list, player_list)
                        break

        if not is_battle_continue(player_list, enemy_list):
            if not player_list:
                return "敵の勝ち！プレーヤーの負け"
            if not enemy_list:
                return "プレーヤーの勝ち！敵の負け"


def battle_main_player(character, target, character_list, player_list, enemy_list):
    print("敵に攻撃しますか？それともHPを回復させますか？\n攻撃なら「1」を回復なら「2」を入力してください")
    main_player_move = input("あなたの行動を教えてください：")
    if main_player_move == "1":
        character.attack(target)
        print(f"\n攻撃：{character.name}　->　{target.name}")
        result_print(character_list)
        if target.HP <= 0:
            enemy_list.remove(target)
    if main_player_move == "2":
        for heal_player in player_list:
            character.heal(heal_player)
        print(f"\n回復：{character.name}と仲間のHP回復")
        result_print(character_list)


def battle_sub_player(character, target, character_list, enemy_list):
    character.attack(target)
    print(f"攻撃：{character.name}　->　{target.name}")
    result_print(character_list)
    if target.HP <= 0:
        enemy_list.remove(target)


def battle_enemy(character, target, character_list, player_list):
    character.attack(target)
    print(f"攻撃：{character.name}　->　{target.name}")
    result_print(character_list)
    if target.HP <= 0:
        player_list.remove(target)
