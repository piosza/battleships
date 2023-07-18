# main game code
import random
import os
from PIL import Image
import sys
import cv2
import time

# from colorama import init, Fore, Back, Style


os.system("cls")


print("<<<<  Game Batlleship   >>>>")


def show_picture(picture_name):
    img = cv2.imread(picture_name, cv2.IMREAD_ANYCOLOR)
    while True:
        cv2.imshow(picture_name, img)
        cv2.waitKey(0)
        break


show_picture("zaglowce.jpg")

#    sys.exit()  # to exit from all the processes


class Player:
    def __init__(self, name):
        self.name = name
        self.number_of_hits = 0


class Warship:
    def __init__(self, length, coordintates):
        self.coordinates = coordintates
        self.length = length
        self.strength_of_ship = length
        self.is_sink = False

    def check_if_hit(self, shot_coordinates):
        if shot_coordinates in self.coordinates and self.is_sink is False:
            print("warship is HIT")
            self.strength_of_ship -= 1
            if self.strength_of_ship == 0:
                self.is_sink = True
                print(" warship is sink")
            return True
        return False


class Board:
    def __init__(self):
        self.forbidden_offsets_1 = (
            (0, 0),
            (-1, -1),
            (0, -1),
            (+1, -1),
            (+1, 0),
            (+1, +1),
            (0, +1),
            (-1, 1),
            (-1, 0),
        )

        self.forbidden_offsets_2_h = (
            (0, 0),
            (+1, 0),
            (-1, -1),
            (0, -1),
            (+1, -1),
            (+2, -1),
            (+2, 0),
            (+2, +1),
            (+1, +1),
            (0, +1),
            (-1, +1),
            (-1, 0),
        )
        self.forbidden_offsets_2_v = (
            (0, 0),
            (0, +1),
            (-1, -1),
            (0, -1),
            (+1, -1),
            (+1, 0),
            (+1, +1),
            (+1, +2),
            (+0, +2),
            (-1, +2),
            (-1, +1),
            (-1, 0),
        )

        self.forbidden_offsets_3_h = (
            (0, 0),
            (+1, 0),
            (+2, 0),
            (-1, -1),
            (0, -1),
            (+1, -1),
            (+2, -1),
            (+3, -1),
            (+3, 0),
            (+3, +1),
            (+2, +1),
            (+1, +1),
            (0, +1),
            (-1, +1),
            (-1, 0),
        )
        self.forbidden_offsets_3_v = (
            (0, 0),
            (0, +1),
            (0, +2),
            (-1, -1),
            (+0, -1),
            (+1, -1),
            (+1, 0),
            (+1, +1),
            (+1, +2),
            (1, +3),
            (0, +3),
            (-1, +3),
            (-1, +2),
            (-1, +1),
            (-1, 0),
        )
        self.forbidden_offsets_4_horizontal = (
            (0, 0),
            (+1, 0),
            (+2, 0),
            (+3, 0),
            (-1, -1),
            (0, -1),
            (+1, -1),
            (+2, -1),
            (+3, -1),
            (+4, -1),
            (-1, 0),
            (+4, 0),
            (-1, +1),
            (0, +1),
            (+1, +1),
            (+2, +1),
            (+3, +1),
            (+4, +1),
        )
        self.forbidden_offsets_4_vertical = (
            (0, 0),
            (0, +1),
            (0, +2),
            (0, +3),
            (-1, -1),
            (0, -1),
            (+1, -1),
            (+1, 0),
            (+1, +1),
            (+1, +2),
            (+1, +3),
            (+1, +4),
            (0, +4),
            (-1, +4),
            (-1, +3),
            (-1, +2),
            (-1, +1),
            (-1, 0),
        )
        self.potential_targets_2 = {(0, -1), (+1, 0), (0, +1), (-1, 0)}
        self.potential_targets_3 = {
            (0, -1),
            (+1, 0),
            (0, +1),
            (-1, 0),
            (0, -2),
            (+2, 0),
            (0, +2),
            (-2, 0),
        }
        self.potential_targets_4 = {
            (0, -1),
            (+1, 0),
            (0, +1),
            (-1, 0),
            (0, -2),
            (+2, 0),
            (0, +2),
            (-2, 0),
            (0, -3),
            (+3, 0),
            (0, +3),
            (-3, 0),
        }
        #        self.forbiden_fields = set()
        self.forbiden_fields = {
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (-1, 0),
            (-1, 1),
            (-1, 2),
            (-1, 3),
            (-1, 4),
            (-1, 5),
            (-1, 6),
            (-1, 7),
            (-1, 8),
            (-1, 9),
            (10, -1),
            (10, 0),
            (10, 1),
            (10, 2),
            (10, 2),
            (10, 3),
            (10, 4),
            (10, 5),
            (10, 6),
            (10, 6),
            (10, 7),
            (10, 8),
            (10, 9),
            (10, 10),
            (10, -10),
            (10, -9),
            (10, -8),
            (10, -7),
            (10, -6),
            (10, -5),
            (10, -4),
            (10, -3),
            (10, -2),
            (10, -1),
            (10, 0),
        }
        self.forbidden_offsets_rest = {(-1, -1), (+1, -1), (+1, +1), (-1, +1)}
        self.state = [["_" for i in range(10)] for j in range(10)]

    def __str__(self):
        return """
      0 1 2 3 4 5 6 7 8 9x
    0|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|
    1|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|
    2|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|
    3|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|
    4|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|
    5|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|
    6|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|
    7|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|
    8|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|
    9|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|
    y
    """.format(
            *sum(self.state, [])
        )


computer_warships = []
human_warships = []

board1 = Board()

# print(board1)

# ############################################## computer ###########################################################
# #################################################################################################


print("computer deployment of ships ")
board2 = Board()
board4 = Board()
board3 = Board()

# 4

i = 0
while i < 1:
    placement = random.choice(("Horizontal", "Vertical"))

    if placement == "Horizontal":
        x = int(random.randint(0, 6))
        y = int(random.randint(0, 9))
        # if (x, y) in board2.forbiden_fields or (
        #     x + 1,
        #     x + 2,
        #     x + 3,
        #     y + 0,
        # ) in board2.forbiden_fields:
        #     continue
        board2.state[y][x] = "4"
        board2.state[y][x + 1] = "4"
        board2.state[y][x + 2] = "4"
        board2.state[y][x + 3] = "4"

        ship = Warship(4, [(x, y), (x + 1, y), (x + 2, y), (x + 3, y)])
        computer_warships.append(ship)
        #        Warship(4,coordintates=[(x,y),(x+1,y),(x+2,y),(x+3,y)])
        board2.forbiden_fields.add((x, y))
        for offsets in board2.forbidden_offsets_4_horizontal:
            xo, yo = offsets
            board2.forbiden_fields.add((x + xo, y + yo))
    elif placement == "Vertical":
        x = int(random.randint(0, 9))
        y = int(random.randint(0, 6))
        board2.state[y][x] = "4"
        board2.state[y + 1][x + 0] = "4"
        board2.state[y + 2][x + 0] = "4"
        board2.state[y + 3][x + 0] = "4"
        ship = Warship(4, [(x, y), (x, y + 1), (x, y + 2), (x, y + 3)])
        computer_warships.append(ship)
        board2.forbiden_fields.add((x, y))

        for offsets in board2.forbidden_offsets_4_vertical:
            xo, yo = offsets
            board2.forbiden_fields.add((x + xo, y + yo))

    i += 1
    print(board2)

# # 3

i = 0
while i < 2:
    placement = random.choice(("Horizontal3", "Vertical3"))
    if placement == "Horizontal3":
        x = int(random.randint(0, 7))
        y = int(random.randint(0, 9))
        if (
            (x, y) in board2.forbiden_fields
            or (x + 1, y) in board2.forbiden_fields
            or (x + 2, y) in board2.forbiden_fields
            or (x + 3, y) in board2.forbiden_fields
        ):
            continue
        board2.state[y][x] = "3"
        board2.state[y][x + 1] = "3"
        board2.state[y][x + 2] = "3"
        ship = Warship(3, [(x, y), (x + 1, y), (x + 2, y)])
        computer_warships.append(ship)
        board2.forbiden_fields.add((x, y))
        for offsets in board2.forbidden_offsets_3_h:
            xo, yo = offsets
            board2.forbiden_fields.add((x + xo, y + yo))
    elif placement == "Vertical3":
        x = int(random.randint(0, 9))
        y = int(random.randint(0, 7))
        if (
            (x, y) in board2.forbiden_fields
            or (x, y + 1) in board2.forbiden_fields
            or (x, y + 2) in board2.forbiden_fields
            or (x, y + 3) in board2.forbiden_fields
        ):
            continue
        board2.state[y][x] = "3"
        board2.state[y + 1][x + 0] = "3"
        board2.state[y + 2][x + 0] = "3"
        board2.forbiden_fields.add((x, y))
        ship = Warship(3, [(x, y), (x, y + 1), (x, y + 2)])
        computer_warships.append(ship)
        for offsets in board2.forbidden_offsets_3_v:
            xo, yo = offsets
            board2.forbiden_fields.add((x + xo, y + yo))

    i += 1
    print(board2)
# # 2

i = 0
while i < 3:
    placement = random.choice(("Horizontal2", "Vertical2"))
    if placement == "Horizontal2":
        x = int(random.randint(0, 7))
        y = int(random.randint(0, 7))
        if (x, y) in board2.forbiden_fields or (x + 1, y) in board2.forbiden_fields:
            continue
        board2.state[y][x] = "2"
        board2.state[y][x + 1] = "2"
        ship = Warship(2, [(x, y), (x + 1, y)])
        computer_warships.append(ship)
        board2.forbiden_fields.add((x, y))
        for offsets in board2.forbidden_offsets_2_h:
            xo, yo = offsets
            board2.forbiden_fields.add((x + xo, y + yo))
    elif placement == "Vertical2":
        x = int(random.randint(0, 7))
        y = int(random.randint(0, 7))
        if (x, y) in board2.forbiden_fields or (x, y + 1) in board2.forbiden_fields:
            continue
        board2.state[y][x] = "2"
        board2.state[y + 1][x + 0] = "2"
        ship = Warship(2, [(x, y), (x, y + 1)])
        computer_warships.append(ship)
        board2.forbiden_fields.add((x, y))
        for offsets in board2.forbidden_offsets_2_v:
            xo, yo = offsets
            board2.forbiden_fields.add((x + xo, y + yo))
    i += 1
    print(board2)

# # # 1

i = 0
while i < 4:
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 9))
    if (x, y) in board2.forbiden_fields:
        continue
    board2.state[y][x] = "1"
    board2.forbiden_fields.add((x, y))
    ship = Warship(1, [(x, y)])
    computer_warships.append(ship)
    for offsets in board2.forbidden_offsets_1:
        xo, yo = offsets
        board2.forbiden_fields.add((x + xo, y + yo))
    i += 1


print(board2)


# #################################################### HUMAN ###################################
# 4

i = 0
while i < 1:
    placement = random.choice(("Horizontal", "Vertical"))

    if placement == "Horizontal":
        x = int(random.randint(0, 6))
        y = int(random.randint(0, 9))
        # if (x, y) in board2.forbiden_fields or (
        #     x + 1,
        #     x + 2,
        #     x + 3,
        #     y + 0,
        # ) in board2.forbiden_fields:
        #     continue
        board1.state[y][x] = "4"
        board1.state[y][x + 1] = "4"
        board1.state[y][x + 2] = "4"
        board1.state[y][x + 3] = "4"

        ship = Warship(4, [(x, y), (x + 1, y), (x + 2, y), (x + 3, y)])
        human_warships.append(ship)
        #        Warship(4,coordintates=[(x,y),(x+1,y),(x+2,y),(x+3,y)])
        board1.forbiden_fields.add((x, y))
        for offsets in board1.forbidden_offsets_4_horizontal:
            xo, yo = offsets
            board1.forbiden_fields.add((x + xo, y + yo))

    elif placement == "Vertical":
        x = int(random.randint(0, 9))
        y = int(random.randint(0, 6))
        board1.state[y][x] = "4"
        board1.state[y + 1][x + 0] = "4"
        board1.state[y + 2][x + 0] = "4"
        board1.state[y + 3][x + 0] = "4"
        ship = Warship(4, [(x, y), (x, y + 1), (x, y + 2), (x, y + 3)])
        human_warships.append(ship)
        board1.forbiden_fields.add((x, y))

        for offsets in board1.forbidden_offsets_4_vertical:
            xo, yo = offsets
            board1.forbiden_fields.add((x + xo, y + yo))

    i += 1


# # 3

i = 0
while i < 2:
    placement = random.choice(("Horizontal3", "Vertical3"))
    if placement == "Horizontal3":
        x = int(random.randint(0, 7))
        y = int(random.randint(0, 9))
        if (
            (x, y) in board1.forbiden_fields
            or (x + 1, y) in board1.forbiden_fields
            or (x + 2, y) in board1.forbiden_fields
            or (x + 3, y) in board1.forbiden_fields
        ):
            continue
        board1.state[y][x] = "3"
        board1.state[y][x + 1] = "3"
        board1.state[y][x + 2] = "3"
        ship = Warship(3, [(x, y), (x + 1, y), (x + 2, y)])
        human_warships.append(ship)
        board1.forbiden_fields.add((x, y))
        for offsets in board1.forbidden_offsets_3_h:
            xo, yo = offsets
            board1.forbiden_fields.add((x + xo, y + yo))
    elif placement == "Vertical3":
        x = int(random.randint(0, 9))
        y = int(random.randint(0, 7))
        if (
            (x, y) in board1.forbiden_fields
            or (x, y + 1) in board1.forbiden_fields
            or (x, y + 2) in board1.forbiden_fields
            or (x, y + 3) in board1.forbiden_fields
        ):
            continue
        board1.state[y][x] = "3"
        board1.state[y + 1][x + 0] = "3"
        board1.state[y + 2][x + 0] = "3"
        board1.forbiden_fields.add((x, y))
        ship = Warship(3, [(x, y), (x, y + 1), (x, y + 2)])
        human_warships.append(ship)
        for offsets in board1.forbidden_offsets_3_v:
            xo, yo = offsets
            board1.forbiden_fields.add((x + xo, y + yo))

    i += 1

# # 2

i = 0
while i < 3:
    placement = random.choice(("Horizontal2", "Vertical2"))
    if placement == "Horizontal2":
        x = int(random.randint(0, 7))
        y = int(random.randint(0, 7))
        if (x, y) in board1.forbiden_fields or (x + 1, y) in board1.forbiden_fields:
            continue
        board1.state[y][x] = "2"
        board1.state[y][x + 1] = "2"
        ship = Warship(2, [(x, y), (x + 1, y)])
        human_warships.append(ship)
        board1.forbiden_fields.add((x, y))
        for offsets in board1.forbidden_offsets_2_h:
            xo, yo = offsets
            board1.forbiden_fields.add((x + xo, y + yo))
    elif placement == "Vertical2":
        x = int(random.randint(0, 7))
        y = int(random.randint(0, 7))
        if (x, y) in board1.forbiden_fields or (x, y + 1) in board1.forbiden_fields:
            continue
        board1.state[y][x] = "2"
        board1.state[y + 1][x + 0] = "2"
        ship = Warship(2, [(x, y), (x, y + 1)])
        human_warships.append(ship)
        board1.forbiden_fields.add((x, y))
        for offsets in board1.forbidden_offsets_2_v:
            xo, yo = offsets
            board1.forbiden_fields.add((x + xo, y + yo))
    i += 1
    print(board2)

# # # 1

i = 0
while i < 4:
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 9))
    if (x, y) in board1.forbiden_fields:
        continue
    board1.state[y][x] = "1"
    board1.forbiden_fields.add((x, y))
    ship = Warship(1, [(x, y)])
    human_warships.append(ship)
    for offsets in board1.forbidden_offsets_1:
        xo, yo = offsets
        board1.forbiden_fields.add((x + xo, y + yo))
    i += 1

print("Computer board")
print(board2)
print("Human board")
print(board1)
print("board deployment ready !!")
print("lets make sea battle")


############################################# GAME ######################################################


def receive_attack(self, coordinates):
    x, y = coordinates
    if self.state[y][x] == "_":
        print(" missed gun fire  ")
    else:
        print("warship hitted")


def computer_cannon_volley(player):
    allowed_shots = []
    while True:
        if player.number_of_hits <= 20:
            if not allowed_shots:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
            else:
                x, y = allowed_shots.pop

            if (x, y) in board4.forbiden_fields:
                continue
            if board1.state[y][x] == "_":
                board4.state[y][x] = "m"
            if board1.state[y][x] == "1":
                board4.state[y][x] = "s"
                board4.forbiden_fields.add((x, y))
                player.number_of_hits += 1
                for offsets in board1.forbidden_offsets_1:
                    xo, yo = offsets
                    board4.forbiden_fields.add((x + xo, y + yo))
                show_picture("hit.jpg")
            if (
                board1.state[y][x] == "2"
                or board1.state[y][x] == "3"
                or board1.state[y][x] == "4"
            ):
                for offsets in board1.forbidden_offsets_rest:
                    xo, yo = offsets
                    board4.forbiden_fields.add((x + xo, y + yo))
                show_picture("hit.jpg")

            #               for potential_target in board4.potential_targets_2:

            for warship in human_warships:
                if warship.check_if_hit((x, y)):
                    board4.forbiden_fields.add((x, y))
                    board4.state[y][x] = "h"
                    if warship.is_sink:
                        for single_coordinate in warship.coordinates:
                            x_, y_ = single_coordinate
                            board4.state[y_][x_] = "s"
                            player.number_of_hits += 1
                            print(x_, y_)
                            # img = cv2.imread("sunk.jpg", cv2.IMREAD_ANYCOLOR)
                            # while True:
                            #     cv2.imshow("sunk.jpg", img)
                            #     cv2.waitKey(0)
                            #     break
            #            print(board4)
            time.sleep(0.5)
            print("computer view of the targets ")
            break


# def computer_cannon_volley(player):
#     if board4.state[y][x] == "h":
#         for potential_target in board4.potential_targets_2:
#             xo, yo = potential_target
#             board4.potential_targets_2.add((x + xo, y + yo))
#             x = int(random.randint(0, 9))
#             y = int(random.randint(0, 9))
#             if board4.state[y][x] in board4.potential_targets_2:
#                 if board1.state[y][x] == "_":
#                     board4.state[y][x] = "m"
#                 if board1.state[y][x] == "1":
#                     board4.state[y][x] = "s"
#                     player.number_of_hits += 1
#                     for offsets in board1.forbidden_offsets_1:
#                         xo, yo = offsets
#                     board4.forbiden_fields.add((x + xo, y + yo))
#                     if board4.state[y][x] == "h":
#                         player.number_of_hits += 1

#     if board4.state[y][x] == "h" and board4.state[y][x] == "h":
#         for potential_target in board4.potential_targets_3:
#             xo, yo = potential_target
#             board4.potential_targets_2.add((x + xo, y + yo))
#             x = int(random.randint(0, 9))
#             y = int(random.randint(0, 9))
#             if board4.state[y][x] in board4.potential_targets_3:
#                 if board1.state[y][x] == "_":
#                     board4.state[y][x] = "m"
#                 if board4.state[y][x] == "h":
#                     player.number_of_hits += 1
#                     if board4.state[y][x] == "h":
#                         board4.state[y][x] = "s"

#     if (
#         board4.state[y][x] == "h"
#         and board4.state[y][x] == "h"
#         and board4.state[y][x] == "h"
#     ):
#         for potential_target in board4.potential_targets_4:
#             xo, yo = potential_target
#             board4.potential_targets_2.add((x + xo, y + yo))
#             x = int(random.randint(0, 9))
#             y = int(random.randint(0, 9))
#             if board4.state[y][x] in board4.potential_targets_4:
#                 if board1.state[y][x] == "_":
#                     board4.state[y][x] = "m"
#                     if board4.state[y][x] == "h":
#                         player.number_of_hits += 1
#                         if board4.state[y][x] == "h":
#                             board4.state[y][x] = "s"

#     else:
#         x = int(random.randint(0, 9))
#         y = int(random.randint(0, 9))
#         board4.forbiden_fields.add((x, y))
#         if board2.state[y][x] == "_":
#             board4.state[y][x] = "m"
#         if board2.state[y][x] == "1":
#             board4.state[y][x] = "s"
#             player.number_of_hits += 1
#             for offsets in board1.forbidden_offsets_1:
#                 xo, yo = offsets
#             board4.forbiden_fields.add((x + xo, y + yo))
#         else:
#             board4.state[y][x] = "h"
#             player.number_of_hits += 1

#     board4.forbiden_fields.add((x, y))
#     if board1.state[y][x] == "_":
#         board4.state[y][x] = "m"
#     if board1.state[y][x] == "1":
#         board4.state[y][x] = "s"
#         player.number_of_hits += 1
#         for offsets in board1.forbidden_offsets_1:
#             xo, yo = offsets
#         board4.forbiden_fields.add((x + xo, y + yo))
#     else:
#         board4.state[y][x] == "h"
#         player.number_of_hits += 1


def number_range(start, stop, message):
    while True:
        try:
            a = int(input(message))
        except ValueError:
            continue

        if a in range(start, stop + 1):  # must be 10
            return a


def cannon_volley(player):
    print("cannon_volley")
    x = number_range(0, 9, "set x cannon volley bum (0, 9)")
    y = number_range(0, 9, "set y cannon volley bum (0, 9)")
    while True:
        if (
            board3.state[y][x] == "h"
            or board3.state[y][x] == "s"
            or board3.state[y][x] == "m"
        ):
            print(" missed gun fire  ")
            break
        if board3.state[y][x] == "_":
            print(" missed gun fire  ")
            board3.state[y][x] = "m"

        for warship in computer_warships:
            if warship.check_if_hit((x, y)):
                board3.state[y][x] = "h"
                print("warship is hit")
                if warship.is_sink:
                    for single_coordinate in warship.coordinates:
                        x_, y_ = single_coordinate
                        board3.state[y_][x_] = "s"
                        player.number_of_hits += 1
                        print("warship is sink")
        print(board3)
        print("Human view of the targets ")
        break


def who_win_the_game(hited_c, hited_h):
    if hited_c == 20:
        print("computer win")
    elif hited_h == 20:
        print("sea wolf congratulations victory is yours")


who_first = random.choice(("Comp", "Human"))


print(" Now we begin the battle of ships")

# while hited_c <= 20 or hited_h <= 20:
#         if placement == "Comp":
#             receive_attack()
#         if placement == "Human":
#             cannon_volley()
number_of_turns = 0


def main_game_file():
    player = input(" player name, type here o  -->  ")
    human_player = Player(player)
    computer_player = Player("computer")
    number_of_turns = 0
    while True:
        # a = random.randint(3, 4)
        # if a == 1 or a == 2:
        if number_of_turns % 2 == 1:
            print(f"Started: { human_player.name} next - computer")
            cannon_volley(human_player)
            number_of_turns += 1
        # if a == 3 or a == 4:
        else:
            print(f"Started  computer: next { human_player.name} ")
            computer_cannon_volley(computer_player)
            number_of_turns += 1
        print(number_of_turns)
    # next_run_game_file()
    # else:
    #     print("Human to Human")


# def next_run_game_file(hited_c, hited_h):
#     while True:
#         if hited_c <= 20 or hited_h <= 20:
#             if number_of_turns % 2 == 0:
#                 cannon_volley(player)
#             else:
#                 next_cannon_volley(player)


main_game_file()
