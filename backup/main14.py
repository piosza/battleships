# main game code
import random
import os
from PIL import Image
import sys
import cv2

# from colorama import init, Fore, Back, Style


os.system("cls")


print("<<<<  Game Batlleship   >>>>")
# im = Image.open("zaglowce.jpg")
# im.show()

img = cv2.imread("zaglowce.jpg", cv2.IMREAD_ANYCOLOR)

while True:
    cv2.imshow("zaglowce.jpg", img)
    cv2.waitKey(0)
    break
#    sys.exit()  # to exit from all the processes

cv2.destroyAllWindows()  # destroy all windows


class Warship:
    def __init__(self, length, coordintates):
        self.coordinates = coordintates
        self.length = length

    def __init__(self, length, strength_of_ship, is_sink):
        self.strength_of_ship = strength_of_ship
        self.length = length
        length = strength_of_ship
        is_sink = False


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
        Warship(4, [(x, y), (x + 1, y), (x + 2, y), (x + 3, y)])
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
        Warship(4, [(x, y), (x, y + 1), (x, y + 2), (x, y + 3)])
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
        y = int(random.randint(0, 7))
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
        Warship(3, [(x, y), (x + 1, y), (x + 2, y)])
        board2.forbiden_fields.add((x, y))
        for offsets in board2.forbidden_offsets_3_h:
            xo, yo = offsets
            board2.forbiden_fields.add((x + xo, y + yo))
    elif placement == "Vertical3":
        x = int(random.randint(0, 7))
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
        Warship(3, [(x, y), (x, y + 1), (x, y + 2)])
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
        Warship(2, [(x, y), (x + 1, y)])
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
        Warship(2, [(x, y), (x, y + 1)])
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
    Warship(1, [(x, y)])
    for offsets in board2.forbidden_offsets_1:
        xo, yo = offsets
        board2.forbiden_fields.add((x + xo, y + yo))
    i += 1


print(board2)


# ######################## HUMAN ###################################

print(board1)
print(" Now we begin the deployment of ships")
print("first step, four single-masted ships")
i = 0
while i < 4:
    x = int(input("set x (0-9):  "))
    y = int(input("set y (0-9):  "))
    if (x, y) in board1.forbiden_fields:
        print("fuck what is this ? you  idiot !!!!")
        continue

    board1.state[y][x] = "1"
    board1.forbiden_fields.add((x, y))
    for offsets in board1.forbidden_offsets_1:
        xo, yo = offsets
        board1.forbiden_fields.add((x + xo, y + yo))
        Warship(1, [(x, y)])
    #    print(x, y, board1.forbiden_fields)
    i += 1
    print(board1)
    board1.allowed_places = set()


print("First step ready")
print("   ")
print("second step , there double-masted ships  ")
i = 0
while i < 3:
    x = int(input("set x(0-8):  "))
    y = int(input("set y(0-8):  "))
    placement = input("horizontal or vertical : h, v  >>   ")
    if placement == "h":
        if (x, y) in board1.forbiden_fields:
            print("fuck what is this ? you  idiot !!!!")
            continue
        elif (x + 1, y + 0) in board1.forbiden_fields:
            print("fuck what is this ? you  idiot !!!!")
            continue
        elif x not in range(0, 8) or y not in range(0, 9):
            print("fuck what is this ? you  idiot !!!!")
            continue
        board1.state[y][x] = "2"
        board1.forbiden_fields.add((x, y))
        board1.state[y][x + 1] = "2"
        board1.forbiden_fields.add((x, y))
        Warship(2, [(x, y), (y, x + 1)])
        for offsets in board1.forbidden_offsets_2_h:
            xo, yo = offsets
            board1.forbiden_fields.add((x + xo, y + yo))
    elif placement == "v":
        if (x, y) in board1.forbiden_fields:
            print("fuck what is this ? you  idiot !!!!")
            continue
        elif (
            (x + 0),
            (y + 1),
        ) in board1.forbiden_fields:
            print("fuck what is this ? you  idiot !!!!")
            continue
        board1.state[y][x] = "2"
        board1.forbiden_fields.add((x, y))
        board1.state[y + 1][x + 0] = "2"
        board1.forbiden_fields.add((x + 0, y + 1))
        Warship(2, [(x, y), (x, y + 1)])
        for offsets in board1.forbidden_offsets_2_v:
            xo, yo = offsets
            board1.forbiden_fields.add((x + xo, y + yo))

    else:
        print("very bad choice")
        continue
    print(board1.forbiden_fields)

    i += 1
    print(board1)
print(board1.forbiden_fields)


print("third step, two three-masted ships")

i = 0
while i < 2:
    x = int(input("set x(0-7):  "))
    y = int(input("set y(0-7):  "))
    placement = input("horizontal or vertical : h, v  >>   ")
    if placement == "h":
        if (
            (x, y) in board1.forbiden_fields
            or (x + 1) in board1.forbiden_fields
            or (x + 2) in board1.forbiden_fields
            or (y + 0) in board1.forbiden_fields
        ):
            print("fuck what is this ? you  idiot !!!!")
            continue
        elif x not in range(0, 7) or y not in range(0, 9):
            print("fuck what is this ? you  idiot !!!!")
            continue
        board1.state[y][x] = "3"
        board1.state[y][x + 1] = "3"
        board1.state[y][x + 2] = "3"
        Warship(3, [(x, y), (x + 1, y), (x + 2, y)])
        board1.forbiden_fields.add((x, y))
        for offsets in board1.forbidden_offsets_3_h:
            xo, yo = offsets
            board1.forbiden_fields.add((x + xo, y + yo))
    elif placement == "v":
        if (
            (x, y) in board1.forbiden_fields
            or (x + 0) in board1.forbiden_fields
            or (y + 1) in board1.forbiden_fields
            or (y + 2) in board1.forbiden_fields
        ):
            print("fuck what is this ? you  idiot !!!!")
            continue
        elif x not in range(0, 9) or y not in range(0, 8):
            print("fuck what is this ? you  idiot !!!!")
            continue
        board1.state[y][x] = "3"
        board1.state[y + 1][x + 0] = "3"
        board1.state[y + 2][x + 0] = "3"
        Warship(3, [(x, y), (x, y + 1), (x, y + 2)])
        board1.forbiden_fields.add((x, y))
        for offsets in board1.forbidden_offsets_3_v:
            xo, yo = offsets
            board1.forbiden_fields.add((x + xo, y + yo))

    else:
        print("very bad choice")
        continue

    i += 1
    print(board1)


print("last step, one four-masted ships")

i = 0
while i < 1:
    x = int(input("set x(0-6):  "))
    y = int(input("set y(0-6):  "))
    placement = input("horizontal or vertical : h, v  >>   ")
    if placement == "h":
        if (x, y) in board1.forbiden_fields or (
            x + 1,
            x + 2,
            x + 3,
            y + 0,
        ) in board1.forbiden_fields:
            print("fuck what is this ? you  idiot !!!!")
            continue
        elif x not in range(0, 6) or y not in range(0, 9):
            print("fuck what is this ? you  idiot !!!!")
            continue
        board1.state[y][x] = "4"
        board1.state[y][x + 1] = "4"
        board1.state[y][x + 2] = "4"
        board1.state[y][x + 3] = "4"
        Warship(4, [(x, y), (x + 1, y), (x + 2, y), (x + 3, y)])
        board1.forbiden_fields.add((x, y))

    elif placement == "v":
        if (x, y) in board1.forbiden_fields or (
            x + 0,
            y + 1,
            y + 2,
            y + 3,
        ) in board1.forbiden_fields:
            print("fuck what is this ? you  idiot !!!!")
            continue
        elif x not in range(0, 9) or y not in range(0, 6):
            print("fuck what is this ? you  idiot !!!!")
            continue
        board1.state[y][x] = "4"
        board1.state[y + 1][x + 0] = "4"
        board1.state[y + 2][x + 0] = "4"
        board1.state[y + 3][x + 0] = "4"
        Warship(4, [(x, y), (x, y + 1), (x, y + 2), (x, y + 3)])
        board1.forbiden_fields.add((x, y))

    else:
        print("very bad choice, you really vant do it good ? ")
        continue

    i += 1
    print("board deployment ready !!")
    print(board1)
    print("lets make sea battle")


############################################# GAME ######################################################

hited_c = 0
hited_h = 0


def receive_attack(self, coordinates):
    x, y = coordinates
    if self.state[y][x] == "_":
        print(" missed gun fire  ")
    else:
        print("warship hitted")


def first_cannon_volley(board, coordinates_of_hit, hited_h):
    x, y = coordinates_of_hit
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 9))
    if board1.state[y][x] == "_":
        board3.state[y][x] = "m"
    if board1.state[y][x] == "1":
        board3.state[y][x] = "s"
        hited_h += 1
        for offsets in board.forbidden_offsets_1:
            xo, yo = offsets
        board3.forbiden_fields.add((x + xo, y + yo))
    else:
        board4.state[y][x] = "h"
        hited_h += 1


def cannon_volley():
    print("cannon_volley")
    x = int(input("set x cannon_volley buum (0-9):  "))
    y = int(input("set y cannon_volley buum (0-9):  "))
    if board2.state[y][x] == "_":
        print(" missed gun fire  ")
        board4.state[y][x] = "m"

    if board2.state[y][x] == "1":
        print("a single-masted ship hit and sunk")
        board4.state[y][x] = "s"
        board2.state[y][x] = "s"
        hited_c += 1
    else:
        print("warship hitted")
        board4.state[y][x] = "h"
        board2.state[y][x] = "h"
        hited_c += 1
    print(board4)


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

cannon_volley()
