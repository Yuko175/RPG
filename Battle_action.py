from Character_data import *
from Character_setup import *
from Battle_action import *
from Battle_other import *
import random


# バトル
def battle(character_list, player_list, enemy_list, main_player_list, sub_player_list):
    turn_count = 0
    while is_battle_continue(player_list, enemy_list):
        turn_count += 1
        print(f"\n☆☆☆☆☆☆☆☆☆{turn_count}ターン☆☆☆☆☆☆☆☆☆\n")
        # キャラクターの行動順をランダムにする
        action_list = random.sample(character_list, len(character_list))
        for character in action_list:
            # キャラクターHPの確認
            if character.HP <= 0:
                print(f"{character.name}のHPがなかったので攻撃できなかった！")
                result_print(character_list)
                continue
            # ターゲットの決定
            for target in action_list:
                if target.HP <= 0:
                    continue
                if character.__class__.__name__ != target.__class__.__name__:
                    # 自ら操作できるキャラクターの動作
                    if character in main_player_list:
                        battle_main_player(
                            character, target, character_list, player_list, enemy_list
                        )
                        break
                    # 仲間の動作
                    elif character in sub_player_list:
                        battle_sub_player(character, target, character_list, enemy_list)
                        break
                    # 敵の動作
                    elif character in enemy_list:
                        battle_enemy(character, target, character_list, player_list)
                        break
    # 勝敗決定
    if not player_list:
        return "敵の勝ち！プレーヤーの負け"
    if not enemy_list:
        return "プレーヤーの勝ち！敵の負け"


# 自ら操作できるキャラクターの動作
def battle_main_player(character, character_list, player_list, enemy_list):
    print("敵に攻撃しますか？それともHPを回復させますか？\n攻撃なら「1」を回復なら「2」を入力してください")
    main_player_move = input("あなたの行動を教えてください：")
    # 攻撃
    if main_player_move == "1":
        battle_main_player_ATK(character, character_list, enemy_list)
    # 回復
    if main_player_move == "2":
        for heal_player in player_list:
            character.heal(heal_player)
        print(f"\n回復：{character.name}と仲間のHP回復")
        result_print(character_list)


# 自ら操作できるキャラクターの動作(攻撃)
def battle_main_player_ATK(character, character_list, enemy_list):
    live_enemy_list = []
    for enemy in enemy_list:
        if enemy.HP > 0:
            live_enemy_list.append(enemy)
    select = True
    while select:
        print("誰に攻撃しますか？数字で回答してください")
        for num, enemy in enumerate(live_enemy_list, 1):
            print(f"{num}：{enemy.name}")
        target_enemy_num = int(input())
        if 1 <= target_enemy_num <= len(live_enemy_list):
            target_enemy_name = live_enemy_list[target_enemy_num - 1]
            character.attack(target_enemy_name)
            print(f"攻撃：{character.name} -> {target_enemy_name.name}")
            result_print(character_list)
            if target_enemy_name.HP <= 0:
                enemy_list.remove(target_enemy_name)
            select = False
        else:
            print("無効なターゲット番号です。正しい番号を選択してください。\n")


# 仲間の動作
def battle_sub_player(character, target, character_list, enemy_list):
    character.attack(target)
    print(f"攻撃：{character.name}　->　{target.name}")
    result_print(character_list)
    if target.HP <= 0:
        enemy_list.remove(target)


# 敵の動作
def battle_enemy(character, target, character_list, player_list):
    character.attack(target)
    print(f"攻撃：{character.name}　->　{target.name}")
    result_print(character_list)
    if target.HP <= 0:
        player_list.remove(target)
