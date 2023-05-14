# main game code
import random
import os

# from colorama import init, Fore, Back, Style


os.system("cls")

print("<<<<  Game Batlleship   >>>>")


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
        self.forbidden_offsets_2_v = (
            (0, 0),
            (+1, 0),
            (-1, -1),
            (0, -1),
            (+1, -1),
            (+2, -1),
            (+2, 0),
            (+2, +0),
            (+2, +1),
            (0, +1),
            (-1, +1),
            (-1, 0),
        )
        self.forbidden_offsets_2_h = (
            (0, 0),
            (0, +1),
            (-1, -1),
            (0, -1),
            (+1, -1),
            (+1, 0),
            (+1, +1),
            (-1, +1),
            (-2, 0),
            (0, -2),
            (2, 0),
            (0, 2),
        )
        self.forbidden_offsets_3 = (
            (-1, -1),
            (0, -1),
            (+1, -1),
            (+1, 0),
            (+1, +1),
            (+1, +2),
            (+1, +3),
            (0, +3),
            (-1, +3),
            (-1, +2),
            (-1, +1),
            (-1, 0),
        )
        self.forbidden_offsets_3_v = (
            (0, 0),
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
        self.forbidden_offsets_3_h = (
            (0, 0),
            (-1, -1),
            (0, -1),
            (+1, -1),
            (+1, 0),
            (+1, +1),
            (+1, +2),
            (+1, +3),
            (0, +3),
            (-1, +3),
            (-1, +2),
            (-1, +2),
            (-1, 0),
        )

        self.forbidden_offsets_4_horizontal = (
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
            (-1, -1),
            (0, -1),
            (+1, -1),
            (+1, 0),
            (+1, +1),
            (+1, +2),
            (+1, +3),
            (0, +4),
            (-1, +3),
            (-1, +2),
            (-1, +1),
            (-1, 0),
            (-1, 4),
            (1, 4),
        )
        self.allowed_places_2 = ((+1, 0), (0, +1), (-1, 0), (0, -1))
        self.allowed_places_3 = (
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
        )

        self.allowed_places_3_1 = ((0, +1), (0, +2), (0, +3))

        self.allowed_places_3_2 = ((0, +1), (0, +2), (0, +3))

        #       ((+1, +0), (+2, +0), (+3, +0))
        #       ((0, +1), (0, +2), (0, +3))
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

        self.allowed_places_4_horizontal = ((0, 0), (+1, 0), (+2, 0), (+3, 0))
        self.allowed_places_4_vertical = ((0, 0), (0, +1), (0, +2), (0, +3))

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

# print(board1)


print("computer deployment of ships ")
board2 = Board()


# 4

i = 0
while i < 1:
    placement = random.choice(("Horizontal", "Vertical"))
    print(placement)
    if placement == "Horizontal":
        allowed_offsets = board2.allowed_places_4_horizontal
        x = int(random.randint(0, 3))
        y = int(random.randint(0, 9))
        forbiden_offsets = board2.forbidden_offsets_4_horizontal
    else:
        allowed_offsets = board2.allowed_places_4_vertical
        x = int(random.randint(0, 9))
        y = int(random.randint(0, 3))
        forbiden_offsets = board2.forbidden_offsets_4_vertical
    if (x, y) in board2.forbiden_fields:
        continue
    board2.state[y][x] = "4"
    for allows in allowed_offsets:
        xo, yo = allows
        board2.allowed_places.add((x + xo, y + yo))
    print(x, y, board2.allowed_places)
    #    print(board2.allowed_places)
    board2.forbiden_fields.add((x, y))
    for offsets in forbiden_offsets:
        xo, yo = offsets
        board2.forbiden_fields.add((x + xo, y + yo))
    i += 1

i = 0
while i < 3:
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 9))
    if (x, y) in board2.forbiden_fields:
        continue
    if (x, y) not in board2.allowed_places:
        continue
    board2.state[y][x] = "4"
    board2.forbiden_fields.add((x, y))

    i += 1


# 3_1

i = 0
while i < 1:
    x = int(random.randint(0, 9))
    y = int(random.randint(0, 6))
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
    # for offsets in board2.forbidden_offsets_3:
    #     xo, yo = offsets
    #     board2.forbiden_fields.add((x + xo, y + yo))
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

    # for offsets in board2.forbidden_offsets_3:
    #     xo, yo = offsets
    #     board2.forbiden_fields.add((x + xo, y + yo))
    #     board2.forbiden_fields.add((x, y))
    i += 1
board2.allowed_places = set()

# 3_2

i = 0
while i < 1:
    x = int(random.randint(0, 6))
    y = int(random.randint(0, 6))
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
    x = int(random.randint(0, 8))
    y = int(random.randint(0, 8))

    if (x, y) in board2.forbiden_fields:
        continue
    if (x, y) not in board2.allowed_places:
        continue
    board2.state[y][x] = "3"
    board2.forbiden_fields.add((x, y))

    i += 1
board2.allowed_places = set()

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

# # 1

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


# ######################## HUMAN ###################################

print(board1)
print(" Now we begin the deployment of ships")
print("first step, four single-masted ships")
i = 0
while i < 4:
    x = int(input("x(0-9):  "))
    y = int(input("y(0-9):  "))
    #    print(x,y,board1.forbidden_offsets_1)
    if (x, y) in board1.forbiden_fields:
        print("alredy used, or forbiden")
        continue

    board1.state[y][x] = "1"
    board1.forbiden_fields.add((x, y))
    for offsets in board1.forbidden_offsets_1:
        xo, yo = offsets
        board1.forbiden_fields.add((x + xo, y + yo))
    print(x, y, board1.forbiden_fields)
    i += 1
    print(board1)
    board1.allowed_places = set()


print("First step ready")
print("   ")
print("second step , there double-masted ships  ")
i = 0
while i < 3:
    x = int(input("x(0-9):  "))
    y = int(input("y(0-9):  "))
    placement = input("horizontal or vertical : h, v  >>   ")
    if placement == "h":
        if (x, y) in board1.forbiden_fields:
            print("alredy used, or forbiden")
            continue
        elif (x + 1, y + 0) in board1.forbiden_fields:
            print("alredy used, or forbiden")
            continue
        board1.state[y][x] = "2"
        board1.forbiden_fields.add((x, y))
        board1.state[y][x + 1] = "2"
        board1.forbiden_fields.add((x, y))
        for offsets in board1.forbidden_offsets_2_h:
            xo, yo = offsets
            board1.forbiden_fields.add((x + xo, y + yo))
    elif placement == "v":
        if (x, y) in board1.forbiden_fields:
            print("alredy used, or forbiden")
            continue
        elif (
            (x + 0),
            (y + 1),
        ) in board1.forbiden_fields:
            print("alredy used, or forbiden")
            continue
        board1.state[y][x] = "2"
        board1.forbiden_fields.add((x, y))
        board1.state[y + 1][x + 0] = "2"
        board1.forbiden_fields.add((x + 0, y + 1))
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
    x = int(input("x(0-9):  "))
    y = int(input("y(0-9):  "))
    placement = input("horizontal or vertical : h, v  >>   ")
    if placement == "h":
        if (
            (x, y) in board1.forbiden_fields
            or (x + 1) in board1.forbiden_fields
            or (x + 2) in board1.forbiden_fields
            or (y + 0) in board1.forbiden_fields
        ):
            print("alredy used, or forbiden")
            continue
        board1.state[y][x] = "3"
        board1.state[y][x + 1] = "3"
        board1.state[y][x + 2] = "3"
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
            print("alredy used, or forbiden")
            continue
        board1.state[y][x] = "3"
        board1.state[y + 1][x + 0] = "3"
        board1.state[y + 2][x + 0] = "3"
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
    x = int(input("x(0-9):  "))
    y = int(input("y(0-9):  "))
    placement = input("horizontal or vertical : h, v  >>   ")
    if placement == "h":
        if (x, y) in board1.forbiden_fields or (
            x + 1,
            x + 2,
            x + 3,
            y + 0,
        ) in board1.forbiden_fields:
            print("alredy used, or forbiden")
            continue
        board1.state[y][x] = "4"
        board1.state[y][x + 1] = "4"
        board1.state[y][x + 2] = "4"
        board1.state[y][x + 3] = "4"
        board1.forbiden_fields.add((x, y))

    elif placement == "v":
        if (x, y) in board1.forbiden_fields or (
            x + 0,
            y + 1,
            y + 2,
            y + 3,
        ) in board1.forbiden_fields:
            print("alredy used, or forbiden")
            continue
        board1.state[y][x] = "4"
        board1.state[y + 1][x + 0] = "4"
        board1.state[y + 2][x + 0] = "4"
        board1.state[y + 3][x + 0] = "4"
        board1.forbiden_fields.add((x, y))

    else:
        print("very bad choice")
        continue

    i += 1
    print("board deployment ready !!")
    print(board1)
    print("lets make sea battle")
