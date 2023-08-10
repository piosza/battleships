import random
import os
import time
import cv2


os.system("cls")


print("<<<<  Game Batlleship   >>>>")


def show_picture(picture_name):
    img = cv2.imread(picture_name, cv2.IMREAD_ANYCOLOR)
    while True:
        cv2.imshow(picture_name, img)
        cv2.waitKey(0)
        break


show_picture("zaglowce.jpg")


class Player:
    def __init__(
        self,
        name,
    ):
        self.name = name
        self.number_of_hits = 0
        self.allowed_shots = []


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


# ############################################## computer ###########################################################


print("computer deployment of ships ")
board1 = Board()
board2 = Board()
board4 = Board()
board3 = Board()

# # 4

i = 0
while i < 1:
    placement = random.choice(("Horizontal", "Vertical"))

    if placement == "Horizontal":
        x = int(random.randint(0, 6))
        y = int(random.randint(0, 9))

        board2.state[y][x] = "4"
        board2.state[y][x + 1] = "4"
        board2.state[y][x + 2] = "4"
        board2.state[y][x + 3] = "4"

        ship = Warship(4, [(x, y), (x + 1, y), (x + 2, y), (x + 3, y)])
        computer_warships.append(ship)
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

# # 1

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


def selection_game_file():
    layout_selection = input(" 1 auto deployment , 2 human deployment >>>>> ")
    if layout_selection == "1":
        auto_deployment()
    elif layout_selection == "2":
        human_deployment()


def auto_deployment():
    i = 0
    while i < 1:
        placement = random.choice(("Horizontal", "Vertical"))

        if placement == "Horizontal":
            x = int(random.randint(0, 6))
            y = int(random.randint(0, 9))

            board1.state[y][x] = "4"
            board1.state[y][x + 1] = "4"
            board1.state[y][x + 2] = "4"
            board1.state[y][x + 3] = "4"

            ship = Warship(4, [(x, y), (x + 1, y), (x + 2, y), (x + 3, y)])
            human_warships.append(ship)
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
            if (x, y) in board1.forbiden_fields or (
                x + 1,
                y,
            ) in board1.forbiden_fields:
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
            if (x, y) in board1.forbiden_fields or (
                x,
                y + 1,
            ) in board1.forbiden_fields:
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


def human_deployment():
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

        print("Computer board")
        print(board2)
        print("Human board")
        print(board1)
        print("board deployment ready !!")
        print("lets make sea battle")


selection_game_file()
############################################# GAME ######################################################


def receive_attack(self, coordinates):
    x, y = coordinates
    if self.state[y][x] == "_":
        print(" missed gun fire  ")
    else:
        print(" warship hitted ")


def computer_cannon_volley(player: Player, hited_h):
    while True:
        if player.number_of_hits <= 20:
            if player.allowed_shots == []:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
            else:
                x, y = random.choice(player.allowed_shots)
                player.allowed_shots.remove((x, y))

            if (x, y) in board4.forbiden_fields:
                continue
            if board1.state[y][x] == "_":
                board4.state[y][x] = "m"
            if board1.state[y][x] == "1":
                board4.state[y][x] = "s"
                board4.forbiden_fields.add((x, y))
                player.number_of_hits += 1
                hited_h += 1

                for offsets in board1.forbidden_offsets_1:
                    xo, yo = offsets
                    board4.forbiden_fields.add((x + xo, y + yo))
                show_picture("hit.jpg")
            if (
                board1.state[y][x] == "2"
                or board1.state[y][x] == "3"
                or board1.state[y][x] == "4"
            ):
                hited_h += 1

                for offsets in board1.forbidden_offsets_rest:
                    xo, yo = offsets
                    board4.forbiden_fields.add((x + xo, y + yo))
                show_picture("hit.jpg")
            for warship in human_warships:
                if warship.check_if_hit((x, y)):
                    board4.forbiden_fields.add((x, y))
                    board4.state[y][x] = "h"
                    if player.allowed_shots == []:
                        player.allowed_shots.extend(warship.coordinates)
                        player.allowed_shots.remove((x, y))
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
            break
    return hited_h


def number_range(start, stop, message):
    while True:
        try:
            a = int(input(message))
        except ValueError:
            continue

        if a in range(start, stop + 1):  # must be 10
            return a


def cannon_volley(player, hited_h, hited_c):
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
                hited_c += 1
                if warship.is_sink:
                    for single_coordinate in warship.coordinates:
                        x_, y_ = single_coordinate
                        board3.state[y_][x_] = "s"
                        player.number_of_hits += 1
                        print("warship is sink")
        print(board3)
        print("Human view of the targets ")
        print("computer hits human :  ", hited_h)
        print("human hits computer :  ", hited_c)

        break
    return hited_c


who_first = random.choice(("Comp", "Human"))


print(" Now we begin the battle of ships")


def main_game_file():
    print(board1)
    player = input(" player name, type here o  -->  ")
    human_player = Player(player)
    computer_player = Player("computer")
    number_of_turns = 0
    hited_c = 0
    hited_h = 0

    while True:
        if who_win_the_game(hited_c, hited_h, human_player):
            print("game is finish")
            break

        if number_of_turns % 2 == 1:
            print(f"Started: { human_player.name} next - computer")
            hited_c = cannon_volley(human_player, hited_h, hited_c)
            number_of_turns += 1

        else:
            print(f"Started  computer: next { human_player.name} ")
            hited_h = computer_cannon_volley(computer_player, hited_c)
            number_of_turns += 1
        print("number of turns", number_of_turns)
    return human_player


def who_win_the_game(hited_c, hited_h, human_player):
    if hited_h == 20:
        print("computer win")
        return True

    if hited_c == 20:
        print(f"{ human_player.name}  sea wolf congratulations victory is yours")
        return True
    return False


main_game_file()
