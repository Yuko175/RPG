from Battle_action import *


def score_print(turn_count):
    if turn_count <= 7:
        return "S"
    elif turn_count <= 10:
        return "A"
    elif turn_count <= 13:
        return "B"
    elif turn_count <= 16:
        return "C"
    else:
        return "D"
