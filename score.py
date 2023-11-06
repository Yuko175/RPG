from Battle_action import *


def score_print(turn_count):
    if turn_count <= 9:
        return "S"
    elif turn_count <= 12:
        return "A"
    elif turn_count <= 15:
        return "B"
    elif turn_count <= 18:
        return "C"
    else:
        return "D"
