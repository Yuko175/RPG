from Character_data import *


# 自ら操作できるキャラクター
def set_main_player_name(
    character_list, player_list, main_player_name, main_player_list
):
    player = Player(main_player_name)
    character_list.append(player)
    player_list.append(player)
    main_player_list.append(player)


# 仲間
def set_sub_player_name(character_list, player_list, sub_player_list):
    player2 = Player("Player")
    character_list.append(player2)
    player_list.append(player2)
    sub_player_list.append(player2)


# 敵
def set_enemy_name(character_list, enemy_list):
    for i in range(3):
        enemy = Enemy(f"Slime_{i}")
        character_list.append(enemy)
        enemy_list.append(enemy)
