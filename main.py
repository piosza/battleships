# main game code
import random
import os
#from colorama import init, Fore, Back, Style


os.system("cls")

print("<<<<  Game Batlleship   >>>>")

class Board:
    def __init__(self):
        self.state = [['_' for i in range(10)] for j in range(10)]
#board1 =  Board()
#board1.state [5][5] = "x"
#print  (board1.state)
    def __str__(self):
        return  """
      0 1 2 3 4 5 6 7 8 9y
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
    x
    """.format(
        *sum(self.state, [])
    )
board1 =  Board()

print  (board1)

print ("We begin the deployment of ships")
print ("first step, four single-masted ships")
for i in range(4):
    y = int(input("y(0-9):  "))
    x = int(input("x(0-9):  "))
#    if board1.state[x][y] == "1":
#       print(" place alreday used")
#       return False
    board1.state[x][y] = "1"
    print  (board1)
print ("First step ready")
print ("   ")
print ("second step, there double-masted ships")
for i in range(6):
    y = int(input("y(0-9):  "))
    x = int(input("x(0-9):  "))
    board1.state[x][y] = "2"
    print  (board1)
print ("third step, two three-masted ships")
for i in range(6):
    y = int(input("y(0-9):  "))
    x = int(input("x(0-9):  "))
    board1.state[x][y] = "3"
    print  (board1)
print ("last step, one four-masted ships")
for i in range(4):
    y = int(input("y(0-9):  "))
    x = int(input("x(0-9):  "))
    board1.state[x][y] = "4"
    print  (board1)
print ("computer deployment of ships ")
board2 =  Board()
for i in range(4):
    y = random.randint(0,9)
    x = random.randint(0,9)
    board2.state[x][y] = "1"
print  (board2)