from Battle_action import *


def score_print(turn_count):
    if turn_count <= 5:
        return "S"
    elif turn_count <= 8:
        return "A"
    elif turn_count <= 11:
        return "B"
    elif turn_count <= 14:
        return "C"
    else:
        return "D"
