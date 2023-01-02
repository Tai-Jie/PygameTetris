import enum
import random
from Color import*

class Shape(enum.IntEnum):
    I = 1
    O = 2
    T = 3
    S = 4
    Z = 5
    J = 6
    L = 7

class Tetromino():
    
    shape = Shape
    centerX = 0
    centerY = 0
    blocks = []
    color = ()
    next_Shape = Shape
    
    def __init__(self, centerX = 0, centerY = 0) -> None:
        self.next_Shape = random.choice(list(Shape))
        self.randShape()
        self.centerX = centerX
        self.centerY = centerY
    
    def rotation(self):
        if self.shape == Shape.O:
            return       
        # TODO
        # if self.shape == Shape.I:

        for i in range(len(self.blocks)):
            x = self.blocks[i][0]
            y = self.blocks[i][1]
            self.blocks[i] = (-y, x)
    
    def reverseRotation(self):
        if self.shape == Shape.O:
            return
        
        # TODO
        # if self.shape == Shape.I:

        for i in range(len(self.blocks)):
            x = self.blocks[i][0]
            y = self.blocks[i][1]
            self.blocks[i] = (y, -x)

    def randShape(self):
        self.shape = self.next_Shape
        self.next_Shape = random.choice(list(Shape))
        match self.shape:
            case Shape.I:
                self.blocks = [(-1, -1), (0, -1), (1, -1), (-2, -1)]
                self.color = cyan
                # print('tetromino I')

            case Shape.O:
                self.blocks = [(0, -1), (1, -1), (1, 0), (0, 0)]
                self.color = yellow
                # print('tetromino O')

            case Shape.T:
                self.blocks = [(-1, 0), (0, 0), (1, 0), (0, -1)]
                self.color = purple
                # print('tetromino T')
            
            case Shape.S:
                self.blocks = [(-1, 0), (0, 0), (1, -1), (0, -1)]
                self.color = green
                # print('tetromio S')

            case Shape.Z:
                self.blocks = [(1, 0), (0, 0), (-1, -1), (0, -1)]
                self.color = red
                # print('tetromio Z')

            case Shape.J:
                self.blocks = [(-1, -1), (0, 0), (-1, 0), (1, 0)]
                self.color = blue
                # print('tetromio J')
            
            case Shape.L:
                self.blocks = [(1, -1), (0, 0), (1, 0), (-1, 0)]
                self.color = orange
                # print('tetromio L')
