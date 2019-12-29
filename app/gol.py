import numpy as np
import matplotlib.pyplot as plt
from conditionals import *


class GOL:
    def __init__(self, size, figsize, grid):
        self.surrounding = 0  # Keeps track of surrouding alive cells
        self.toLive = []
        self.toDie = []
        self.size = size
        plt.figure(figsize=figsize)

        if len(grid) < 1:
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
        plt.pause(0.1)

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
