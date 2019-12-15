import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

size = 20

class GOL:
    def __init__(self):
        self.surrounding = 0  # Keeps track of surrouding alive cells
        self.toLive = []
        self.toDie = []

    def randomGrid(self):
        # Creates a random size*size grid with 0 or 255 value,
        self.grid = np.random.choice(
            [0, 255], size*size, p=[0.1, 0.9]).reshape(size, size)
        # 0 being off and 255 being on, p is probability off either colour

    def run(self):
        self.randomGrid()
        
        while True:
            # uncomment next line to see the grid updating
            self.showGrid()
            self.checkRules()
            self.applyRules()
            


    def showGrid(self):
        plt.imshow(self.grid)
        plt.pause(0.1)
        
    def applyRules(self):
        for i in range(len(self.toLive)):
            self.grid[self.toLive[i][0]][self.toLive[i][1]] = 0
            
        for i in range(len(self.toDie)):
            self.grid[self.toDie[i][0]][self.toDie[i][1]] = 255
            
        #print(self.grid)
        

    def checkRules(self):
        #print(self.grid)
        for y in range(len(self.grid)):
            for x in range(len(self.grid)):
                self.surrounding = 0

                checkCon = Conditionals(self.grid, y, x)
                checkCon.find()
                
                if checkCon.N:
                    if self.grid[y-1][x] == 0:
                        self.surrounding += 1
                if checkCon.E:
                    if self.grid[y][x+1] == 0:
                        self.surrounding += 1
                if checkCon.S:
                    if self.grid[y+1][x] == 0:
                        self.surrounding += 1
                if checkCon.W:
                    if self.grid[y][x-1] == 0:
                        self.surrounding += 1
                if checkCon.NE:
                    if self.grid[y-1][x+1] == 0:
                        self.surrounding += 1
                if checkCon.SE:
                    if self.grid[y+1][x+1] == 0:
                        self.surrounding += 1
                if checkCon.SW:
                    if self.grid[y+1][x-1] == 0:
                        self.surrounding += 1
                if checkCon.NW:
                    if self.grid[y-1][x-1] == 0:
                        self.surrounding += 1
                #print(y,x,self.surrounding)
                
                
                if self.surrounding < 2 and self.grid[y][x] == 0 and [y,x] not in self.toDie:
                    self.toDie.append([y,x])
                    #self.grid[y][x] = 255
                
                elif self.surrounding == 2 or self.surrounding == 3 and self.grid[y][x] == 0 and [y,x] not in self.toLive:
                    self.toLive.append([y,x])
                    #self.grid[y][x] = 0
                    
                elif self.surrounding > 3 and self.grid[y][x] == 0 and [y,x] not in self.toDie:
                    self.toDie.append([y,x])   
                    #self.grid[y][x] = 255                    
                
                elif self.surrounding == 3 and self.grid[y][x] == 255 and [y,x] not in self.toLive:
                    self.toLive.append([y,x])
                    #self.grid[y][x] = 0

        #print(self.grid)
        #print(self.toLive)
        #print('\n')
        #print(self.toDie)

class Conditionals:

    def __init__(self, grid, y, x):
        self.x = x
        self.y = y
        self.grid = grid
        self.N = False
        self.E = False
        self.S = False
        self.W = False
        self.NE = False
        self.SE = False
        self.SW = False
        self.NW = False

    def find(self):
        # These just check which directions are possible without causing the index to go out of range
        limit = len(self.grid) - 1
        if self.y != 0:
            self.N = True
        if self.x != limit:
            self.E = True
        if self.y != limit:
            self.S = True
        if self.x != 0:
            self.W = True
        if self.N and self.E:
            self. NE = True
        if self.S and self.E:
            self.SE = True
        if self.S and self.W:
            self.SW = True
        if self.N and self.W:
            self.NW = True


test = GOL()
test.run()
