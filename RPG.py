from Character_data import *
from Character_setup import *
from Battle_action import *
from Battle_other import *

"""
ーTODOリストー

・攻撃を選んだ後に回復選択に戻れる
・ロール作り:魔法使い,剣士:防御力,攻撃力

"""


def main():
    # 基本リスト作成
    character_list: list = []
    player_list: list = []
    main_player_list: list = []
    sub_player_list: list = []
    enemy_list: list = []
    main_player_name: str = input("名前を入力してください：")

    # セッティング
    set_main_player_name(
        character_list, player_list, main_player_name, main_player_list
    )
    set_sub_player_name(character_list, player_list, sub_player_list)
    set_enemy_name(character_list, enemy_list)

    # バトルとその結果
    print("\nバトル開始！")
    result_print(character_list)
    battle_result = battle(
        character_list, player_list, enemy_list, main_player_list, sub_player_list
    )
    print(battle_result)


if __name__ == "__main__":
    main()
