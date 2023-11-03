# バトルを続ける条件
def is_battle_continue(player_list, enemy_list):
    if player_list == [] or enemy_list == []:
        return False
    return True


# バトル結果の出力
def result_print(character_list):
    print("--------------")
    for character in character_list:
        if character.HP <= 0:
            print(f"{character.name}：lose")
        elif character.HP > 0:
            print(f"{character.name}：{character.HP}")
    print("--------------\n")
