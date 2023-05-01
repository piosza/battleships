# main game code
import random
import os

# from colorama import init, Fore, Back, Style


os.system("cls")

print("<<<<  Game Batlleship   >>>>")


class Board:
    def __init__(self):
        self.forbidden_offsets_1 = (
            (-1, -1),
            (0, -1),
            (+1, -1),
            (+1, 0),
            (+1, +1),
            (0, +1),
            (-1, 1),
            (-1, 0),
        )
        self.forbidden_offsets_2 = (
            (-1, -1),
            (+1, -1),
            (+1, +1),
            (-1, +1),
            (-2, 0),
            (0, -2),
            (2, 0),
            (0, 2),
        )
        self.forbidden_offsets_3 = (
            (-1, -1),
            (+1, -1),
            (+1, +1),
            (-1, +1),
        )
        self.forbidden_offsets_4 = (
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
        self.allowed_places_2 = ((+1, 0), (0, +1), (-1, 0), (0, -1))
        self.allowed_places_3_1 = ((+1, 0), (+2, 0), (+3, 0))
        self.allowed_places_3_2 = ((0, +1), (0, +2), (0, +3))
        # self.allowed_places_4 = (
        #     (+1, 0),
        #     (0, +1),
        #     (-1, 0),
        #     (0, -1),
        #     (0, -2),
        #     (+2, 0),
        #     (0, +2),
        #     (-2, 0),
        #     (-3, 0),
        #     (0, -3),
        #     (+3, 0),
        #     (0, +3),
        #     (-4, 0),
        #     (0, -4),
        #     (+4, 0),
        #     (0, +4),
        # )

        self.allowed_places_4 = ((0, 0), (+1, 0), (+2, 0), (+3, 0))

        self.state = [["_" for i in range(10)] for j in range(10)]
        self.forbiden_fields = set()
        self.allowed_places = set()

    # board1 =  Board()
    # board1.state [5][5] = "x"
    # print  (board1.state)
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

print(board1)


# print("We begin the deployment of ships")
# print("first step, four single-masted ships")
# i = 0
# while i < 4:

#     x = int(input("x(0-9):  "))
#     y = int(input("y(0-9):  "))
#     #    print(x,y,board1.forbidden_offsets_1)
#     if (x, y) in board1.forbiden_fields:
#         print("alredy used, or forbiden")
#         continue

#     board1.state[y][x] = "1"
#     board1.forbiden_fields.add((x, y))
#     for offsets in board1.forbidden_offsets_1:
#         xo, yo = offsets
#         board1.forbiden_fields.add((x + xo, y + yo))
#     print(x, y, board1.forbidden_offsets_1)
#     i += 1
#     print(board1)
# print("First step ready")
# print("   ")
# print("second step , there double-masted ships  ")
# for _ in range(3):
#     i = 0
#     while i < 2:
#         x = int(input("x(0-9):  "))
#         y = int(input("y(0-9):  "))
#         for allows in board1.allowed_places_2:
#             xo, yo = allows
#             board1.allowed_places.add((x + xo, y + yo))
#         print(x, y, board1.allowed_places)

#         if (x, y) in board1.forbiden_fields:
#             print("alredy used, or forbiden")
#             continue

#         if i >= 1 and (x, y) not in board1.allowed_places:
#             print("wrong place")
#             continue
#         board1.state[y][x] = "2"
#         board1.forbiden_fields.add((x, y))
#         for offsets in board1.forbidden_offsets_2:
#             xo, yo = offsets
#             board1.forbiden_fields.add((x + xo, y + yo))
#         i += 1
#         print(board1)

# print("third step, two three-masted ships")
# for _ in range(2):
#     i = 0
#     while i < 3:
#         x = int(input("x(0-9):  "))
#         y = int(input("y(0-9):  "))
#         for allows in board1.allowed_places_3:
#             xo, yo = allows
#             board1.allowed_places.add((x + xo, y + yo))
#         if (x, y) in board1.forbiden_fields:
#             print("alredy used, or forbiden")
#             continue
#         if (x, y) not in board1.allowed_places:
#             print("wrong place")
#             continue
#         board1.state[y][x] = "3"
#         board1.forbiden_fields.add((x, y))
#         for offsets in board1.forbidden_offsets_2:
#             xo, yo = offsets
#             board1.forbiden_fields.add((x + xo, y + yo))
#         i += 1
#         print(board1)


# print("last step, one four-masted ships")
# for i in range(4):
#     x = int(input("x(0-9):  "))
#     y = int(input("y(0-9):  "))
#     if (x, y) in board1.forbiden_fields:
#         print("alredy used, or forbiden")
#         continue
#     board1.state[y][x] = "4"
#     print(board1)


print("computer deployment of ships ")
board2 = Board()


# 4

i = 0
while i < 1:
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 9))
    if (x, y) in board2.forbiden_fields:
        continue
    board2.state[y][x] = "4"
    for allows in board2.allowed_places_4:
        xo, yo = allows
        board2.allowed_places.add((x + xo, y + yo))

    #    print(board2.allowed_places)
    board2.forbiden_fields.add((x, y))
    for offsets in board2.forbidden_offsets_4:
        xo, yo = offsets
        board2.forbiden_fields.add((x + xo, y + yo))
    i += 1

i = 0
while i < 1:
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 9))
    if (x, y) in board2.forbiden_fields:
        continue
    if (x, y) not in board2.allowed_places:
        continue
    board2.state[y][x] = "4"
    board2.forbiden_fields.add((x, y))

    i += 1

i = 0
while i < 1:
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 9))
    if (x, y) in board2.forbiden_fields:
        continue
    if (x, y) not in board2.allowed_places:
        continue
    board2.state[y][x] = "4"
    board2.forbiden_fields.add((x, y))

    i += 1

i = 0
while i < 1:
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 9))
    if (x, y) in board2.forbiden_fields:
        continue
    if (x, y) not in board2.allowed_places:
        continue
    board2.state[y][x] = "4"
    board2.forbiden_fields.add((x, y))

    i += 1
board2.allowed_places = set()

# 3_1

i = 0
while i < 1:
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 9))
    if (x, y) in board2.forbiden_fields:
        continue

    board2.state[y][x] = "3"
    for allows in board2.allowed_places_3_1:
        xo, yo = allows
        board2.allowed_places.add((x + xo, y + yo))
    board2.forbiden_fields.add((x, y))
    for offsets in board2.forbidden_offsets_3:
        xo, yo = offsets
        board2.forbiden_fields.add((x + xo, y + yo))
    i += 1
i = 0
while i < 1:
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 9))

    if (x, y) in board2.forbiden_fields:
        continue
    if (x, y) not in board2.allowed_places:
        continue
    board2.state[y][x] = "3"
    board2.forbiden_fields.add((x, y))
    for offsets in board2.forbidden_offsets_3:
        xo, yo = offsets
        board2.forbiden_fields.add((x + xo, y + yo))
    i += 1

i = 0
while i < 1:
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 9))

    if (x, y) in board2.forbiden_fields:
        continue
    if (x, y) not in board2.allowed_places:
        continue
    board2.state[y][x] = "3"

    for offsets in board2.forbidden_offsets_3:
        xo, yo = offsets
        board2.forbiden_fields.add((x + xo, y + yo))
        board2.forbiden_fields.add((x, y))
    i += 1


# 3_2

i = 0
while i < 1:
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 9))
    if (x, y) in board2.forbiden_fields:
        continue

    board2.state[y][x] = "3"
    for allows in board2.allowed_places_3_2:
        xo, yo = allows
        board2.allowed_places.add((x + xo, y + yo))
    board2.forbiden_fields.add((x, y))
    for offsets in board2.forbidden_offsets_3:
        xo, yo = offsets
        board2.forbiden_fields.add((x + xo, y + yo))
    i += 1
i = 0
while i < 1:
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 9))

    if (x, y) in board2.forbiden_fields:
        continue
    if (x, y) not in board2.allowed_places:
        continue
    board2.state[y][x] = "3"
    board2.forbiden_fields.add((x, y))

    i += 1

i = 0
while i < 1:
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 9))

    if (x, y) in board2.forbiden_fields:
        continue
    if (x, y) not in board2.allowed_places:
        continue
    board2.state[y][x] = "3"
    board2.forbiden_fields.add((x, y))

    i += 1


# 2

i = 0
while i < 2:
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 9))

    print(x, y, board2.allowed_places)
    print(board2)
    if (x, y) in board2.forbiden_fields:
        continue
    if i >= 1 and (x, y) not in board2.allowed_places:
        continue
    board2.state[y][x] = "2"

    for allows in board2.allowed_places_2:
        xo, yo = allows
        board2.allowed_places.add((x + xo, y + yo))
    board2.forbiden_fields.add((x, y))
    for offsets in board2.forbidden_offsets_2:
        xo, yo = offsets
        board2.forbiden_fields.add((x + xo, y + yo))
    i += 1
board2.allowed_places = set()

i = 0
while i < 2:
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 9))

    print(x, y, board2.allowed_places)
    print(board2)
    if (x, y) in board2.forbiden_fields:
        continue
    if i >= 1 and (x, y) not in board2.allowed_places:
        continue
    board2.state[y][x] = "2"

    for allows in board2.allowed_places_2:
        xo, yo = allows
        board2.allowed_places.add((x + xo, y + yo))
    board2.forbiden_fields.add((x, y))
    for offsets in board2.forbidden_offsets_2:
        xo, yo = offsets
        board2.forbiden_fields.add((x + xo, y + yo))
    i += 1
board2.allowed_places = set()

i = 0
while i < 2:
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 9))

    print(x, y, board2.allowed_places)
    print(board2)
    if (x, y) in board2.forbiden_fields:
        continue
    if i >= 1 and (x, y) not in board2.allowed_places:
        continue
    board2.state[y][x] = "2"

    for allows in board2.allowed_places_2:
        xo, yo = allows
        board2.allowed_places.add((x + xo, y + yo))
    board2.forbiden_fields.add((x, y))
    for offsets in board2.forbidden_offsets_2:
        xo, yo = offsets
        board2.forbiden_fields.add((x + xo, y + yo))
    i += 1
board2.allowed_places = set()

# 1

i = 0
while i < 4:
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 9))
    if (x, y) in board2.forbiden_fields:
        continue
    board2.state[y][x] = "1"
    board2.forbiden_fields.add((x, y))
    for offsets in board2.forbidden_offsets_1:
        xo, yo = offsets
        board2.forbiden_fields.add((x + xo, y + yo))
    #    print(x, y, board2.forbidden_offsets_1)
    i += 1


print(board2)
