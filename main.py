# main game code
import random
import os
#from colorama import init, Fore, Back, Style


os.system("cls")
print()

class Board:
    def __init__(self):
        self.state = [['_' for i in range(10)] for j in range(10)]
#board1 =  Board()
#board1.state [5][5] = "x"
#print  (board1.state)
    def __str__(self):
        return  """
      0 1 2 3 4 5 6 7 8 9
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
    """.format(
        *sum(self.state, [])
    )
board1 =  Board()

print  (board1)

while True:
    x= int(input())
    y= int(input())
    board1.state[x][y] = "#"
    print  (board1)
