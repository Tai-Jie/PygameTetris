from tetromino import*
from Color import*
from Constant import*

class Playfield():
        
    field = list()
    rowNum = list()
    tetromino = Tetromino()
    score = 0
    level = 0
    lines = 0

    def __init__(self) -> None:
        self.field = [[black]*20 for i in range(10)]
        self.rowNum = [i for i in range(20)]
        self.tetromino = Tetromino()
        self.respawnTetrmino()

    def rotate(self):
        self.tetromino.rotation()
        if not self.checkCollision(self.tetromino.centerX, self.tetromino.centerY):
            self.tetromino.reverseRotation()

    def shiftRight(self):
        if self.checkCollision(self.tetromino.centerX + 1, self.tetromino.centerY):
            self.tetromino.centerX += 1

    def shiftLeft(self):
        if self.checkCollision(self.tetromino.centerX - 1, self.tetromino.centerY):
            self.tetromino.centerX -= 1

    def shiftDown(self):
        if self.checkCollision(self.tetromino.centerX, self.tetromino.centerY + 1):
            self.tetromino.centerY += 1

    def drop(self):
        while self.checkCollision(self.tetromino.centerX, self.tetromino.centerY + 1):
            self.tetromino.centerY += 1
    
    def getFieldcolor(self, col, row):
        return self.field[col][self.rowNum[row]]    

    def checkCollision(self, newX, newY) -> bool: # collision -> false
        ground = False
        for block in self.tetromino.blocks:
            if block[0] + newX < 0 or block[0] + newX >= 10 or self.field[block[0] + newX][self.rowNum[block[1] + newY]] != black:
                return False
            
            if block[1] + newY == 20 - 1:
                ground = True
            elif not self.field[block[0] + newX][self.rowNum[block[1] + newY + 1]] == black:
                ground = True

        if ground:
            for block in self.tetromino.blocks:
                self.field[block[0] + newX][self.rowNum[block[1] + newY]] = self.tetromino.color
                # print(block[0] + newX, block[1] + newY, self.field[block[0] + newX][block[1] + newY])
            self.checkfull()
            self.respawnTetrmino()
            return False
        return True

    def checkfull(self):
        combo = 0
        row = 19
        while row >= 0:
            full = True
            for col in range(10):
                if self.field[col][self.rowNum[row]] == black:
                    full = False
            if full:
                combo += 1
                self.lines += 1
                if self.lines == self.getLines_needed2LevelUP():
                    self.level += 1
                # print('removing full row:', row)
                for col in range(10):
                    self.field[col][self.rowNum[row]] = black
                self.rowNum.insert(0, self.rowNum.pop(row))
                # print(self.rowNum)
            else:
                row -= 1
        match combo:
            case 1:
                self.score += 40
            case 2:
                self.score += 100
            case 3:
                self.score += 300
            case 4:
                self.score += 1200
                
    def getScore(self):
        return str(self.score)
    
    def getLines(self):
        return str(self.lines)

    def getLevel(self):
        return str(self.level)

    def getLines_needed2LevelUP(self):
        if self.level <= 9:
            return 5*(self.level**2 + 3*self.level + 2)
        if self.level <= 15:
            return 550 + 100*(self.level-9)
        if self.level == 16:
            return 1260
        if self.level == 17:
            return 1380
        if self.level == 18:
            return 1510
        else:
            return 1510 + 10*(self.level - 18)

    def getFrame_to_Drop(self):
        Frame_to_Drop = [48, 48, 38, 33, 28, 23, 18, 13, 8, 6]
        if self.level <= 9:
            return Frame_to_Drop[self.level]
        if self.level <= 12:
            return 5
        if self.level <= 15:
            return 4
        if self.level <= 18:
            return 3
        if self.level <= 28:
            return 2
        else:
            return 1
         
    def resetField(self):
        self.score = 0
        self.level = 0
        self.lines = 0
        self.field = [[black]*20 for i in range(10)]
        self.rowNum = [i for i in range(20)]
        self.respawnTetrmino()

    def respawnTetrmino(self):
        self.tetromino.randShape()
        self.tetromino.centerX = 5
        self.tetromino.centerY = 1
        for block in self.tetromino.blocks:
            if not self.field[block[0] + 5][self.rowNum[block[1] + 1 + 1]] == black:
                end_event = pygame.event.Event(Game_End)
                print('game end')
                pygame.event.post(end_event)
                break     

    