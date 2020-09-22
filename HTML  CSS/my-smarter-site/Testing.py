class Navi():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def newPos(self, x1, y1):
        self.x = x1
        self.y = y1
    
dot = Navi(0,3)

import numpy as np

a = [[0,0,0,1,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,0],
    [0,1,0,0,0,0,1,0,1,0],
    [0,1,1,1,0,1,1,0,1,0],
    [0,1,0,1,0,1,0,0,1,0],
    [0,1,1,1,1,1,0,1,1,0],
    [0,0,0,0,0,1,0,0,0,0],
    [0,1,0,1,0,1,0,0,1,0],
    [0,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,1,0,0]]


while dot.x != 9 and dot.y != 9:
    if a[dot.x + 1][dot.y] == 1 and a[dot.x][dot.y - 1] != 1 and a[dot.x][dot.y + 1] != 1:
        dot.x += 1
        print(a[dot.x][dot.y])
    elif a[dot.x + 1][dot.y] != 1 and a[dot.x][dot.y - 1] != 1 and a[dot.x][dot.y + 1] == 1:
        dot.y += 1
        print(a[dot.x][dot.y])
    elif a[dot.x + 1][dot.y] != 1 and a[dot.x][dot.y - 1] == 1 and a[dot.x][dot.y + 1] != 1:
        dot.y -= 1
        print(a[dot.x][dot.y])

