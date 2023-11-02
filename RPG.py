from Character_data import *
from Character_setup import *
from Battle_action import *
from Battle_other import *

# 誰を攻撃するか選べる
# ロール:魔法使い,剣士
# 　　　:防御力,攻撃力


def main():
    character_list: list = []
    player_list: list = []
    main_player_list: list = []
    sub_player_list: list = []
    enemy_list: list = []
    main_player_name: str = input("名前を入力してください：")
    set_main_player_name(
        character_list, player_list, main_player_name, main_player_list
    )
    set_sub_player_name(character_list, player_list, sub_player_list)
    set_enemy_name(character_list, enemy_list)

    print(
        battle(
            character_list, player_list, enemy_list, main_player_list, sub_player_list
        )
    )


if __name__ == "__main__":
    main()
