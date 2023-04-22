# main game code
import random
import os
#from colorama import init, Fore, Back, Style


os.system("cls")

print("<<<<  Game Batlleship   >>>>")

class Board:
    
    def __init__(self):
        self.forbidden_offsets_1 = ((-1,-1),(0,-1),(+1,-1),(+1,0),(+1,+1),(0,+1),(-1,1),(-1,0))
        self.forbidden_offsets_2 = ((-1,-1),(+1,-1),(+1,+1),(-1,+1))
        self.allowed_places_2 = ((+1,0),(0,+1),(-1,0),(0,-1))
        self.state = [['_' for i in range(10)] for j in range(10)]
        self.forbiden_fields = set()
        self.allowed_places = set()
        


#board1 =  Board()
#board1.state [5][5] = "x"
#print  (board1.state)
    def __str__(self):
        return  """
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
board1 =  Board()

print  (board1)


print ("We begin the deployment of ships")
print ("first step, four single-masted ships")
i = 0
while i<4 :


    x = int(input("x(0-9):  "))
    y = int(input("y(0-9):  "))
#    print(x,y,board1.forbidden_offsets_1)
    if (x,y) in board1.forbiden_fields:
        print("alredy used, or forbiden")
        continue

    board1.state[y][x] = "1"
    board1.forbiden_fields.add((x,y))
    for offsets in board1.forbidden_offsets_1:
        xo, yo = offsets
        board1.forbiden_fields.add((x+xo,y+yo))
    i+=1    
    print  (board1)

print ("First step ready")
print ("   ")
print ("second step 1, there double-masted ships first ship ")
for i in range(2):
    x = int(input("x(0-9):  "))
    for allows in board1.allowed_places_2:
        xo, yo = allows
        board1.allowed_places.add((x+xo,y+yo))
    y = int(input("y(0-9):  "))
    print(x,y,board1.allowed_places_2)
    if (x,y) not in board1.allowed_places_2:
        print("wrong place ")
        continue
    if (x,y) in board1.forbiden_fields:
        print("alredy used, or forbiden")
        continue
    
    board1.state[x][y] = "2"
    board1.forbiden_fields.add((x,y))
    for offsets in Board.forbidden_offsets_2:
        xo, yo = offsets
        board1.forbiden_fields.add((x+xo,y+yo))
    print  (board1)
print ("second step 2, there double-masted ships second ship ")
for i in range(2):
    x = int(input("x(0-9):  "))
    y = int(input("y(0-9):  "))
    if (x,y) in board1.forbiden_fields:
        print("alredy used, or forbiden")
        continue
    board1.state[x][y] = "2"
    board1.forbiden_fields.add((x,y))
    for offsets in Board.forbidden_offsets_2:
        xo, yo = offsets
        board1.forbiden_fields.add((x+xo,y+yo))
    print  (board1)
print ("second step 3, there double-masted ships third ship ")
for i in range(2):
    x = int(input("x(0-9):  "))
    y = int(input("y(0-9):  "))
    if (x,y) in board1.forbiden_fields:
        print("alredy used, or forbiden")
        continue
    board1.state[x][y] = "2"
    board1.forbiden_fields.add((x,y))
    for offsets in Board.forbidden_offsets_2:
        xo, yo = offsets
        board1.forbiden_fields.add((x+xo,y+yo))
    print  (board1)    
print ("third step, two three-masted ships")
for i in range(6):
    x = int(input("x(0-9):  "))
    y = int(input("y(0-9):  "))
    if (x,y) in board1.forbiden_fields:
        print("alredy used, or forbiden")
        continue
    board1.state[x][y] = "3"
    print  (board1)
print ("last step, one four-masted ships")
for i in range(4):
    x = int(input("x(0-9):  "))
    y = int(input("y(0-9):  "))
    if (x,y) in board1.forbiden_fields:
        print("alredy used, or forbiden")
        continue
    board1.state[x][y] = "4"
    print  (board1)
print ("computer deployment of ships ")
board2 =  Board()
for i in range(4):
    x = int(input("x(0-9):  "))
    y = int(input("y(0-9):  "))
    board2.state[x][y] = "1"
print  (board2)