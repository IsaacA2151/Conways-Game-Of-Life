import numpy as np
import matplotlib.pyplot as plt


class GOL:
    def __init__(self, size, figsize, grid):
        self.surrounding = 0  # Keeps track of surrouding alive cells
        self.toLive = []
        self.toDie = []
        self.size = size
        plt.figure(figsize=figsize)

        if grid is None:
            self.grid = np.random.choice([0, 255], self.size*self.size, p=[0.1, 0.9]).reshape(self.size, self.size)
        else:
            self.grid = grid

    def run(self):
        while True:
            self.toDie = []
            self.toLive = []
            self.showGrid()
            self.checkRules()
            self.applyRules()

    def showGrid(self):
        plt.imshow(self.grid)
        plt.pause(0.01)

    def applyRules(self):
        for i in self.toLive:
            self.grid[i[0]][i[1]] = 0

        for i in self.toDie:
            self.grid[i[0]][i[1]] = 255

    def checkRules(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid)):
                self.surrounding = 0

                checkCon = Conditionals(self.grid, y, x)
                checkCon.checkEnv()

                if checkCon.N and self.grid[y-1][x] == 0:
                    self.surrounding += 1
                if checkCon.E and self.grid[y][x+1] == 0:
                    self.surrounding += 1
                if checkCon.S and self.grid[y+1][x] == 0:
                    self.surrounding += 1
                if checkCon.W and self.grid[y][x-1] == 0:
                    self.surrounding += 1
                if checkCon.NE and self.grid[y-1][x+1] == 0:
                    self.surrounding += 1
                if checkCon.SE and self.grid[y+1][x+1] == 0:
                    self.surrounding += 1
                if checkCon.SW and self.grid[y+1][x-1] == 0:
                    self.surrounding += 1
                if checkCon.NW and self.grid[y-1][x-1] == 0:
                    self.surrounding += 1

                del checkCon

                if self.surrounding == 3 and self.grid[y][x] == 255:
                    self.toLive.append([y, x])
                elif self.grid[y][x] == 0 and self.surrounding not in (2, 3):
                    self.toDie.append([y, x])


class Conditionals:

    def __init__(self, grid, y, x):
        self.x = x
        self.y = y
        self.grid = grid
        self.N = True
        self.E = True
        self.S = True
        self.W = True
        self.NE = False
        self.SE = False
        self.SW = False
        self.NW = False

    def checkEnv(self):
        limit = len(self.grid) - 1
        if self.y == 0:
            self.N = False
        elif self.y == limit:
            self.S = False
        if self.x == 0:
            self.W = False
        elif self.x == limit:
            self.E = False

        if self.N and self.E:
            self. NE = True
        if self.S and self.E:
            self.SE = True
        if self.S and self.W:
            self.SW = True
        if self.N and self.W:
            self.NW = True


config = {
    'size': 100,
    'figsize': (10, 10),
    'grid': None,
}

test = GOL(**config)
test.run()
