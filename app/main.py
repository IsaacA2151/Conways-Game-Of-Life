import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

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

class Panel:

    def __init__(self,grid,d=None):
        self.grid = grid
        self.changed = True
        if d != None:
              self.changed = False
              self.dimensions = d
              
        self.width = 800
        self.height = 800
        self.yCords = []
        self.xCords = []

    def control(self):
        window = Tk()
        Label(window,text='Enter Size Of Grid:').pack()
        self.dimensions = Entry(window)
        self.dimensions.pack()
        Button(window,text='Create Grid',command=self.makeGrid).pack()
        window.mainloop()
            
    def makeGrid(self):
        self.gridWindow = Tk()
        self.w = Canvas(self.gridWindow,width=self.width,height=self.height)
        self.w.pack()
        
        if self.changed:
              try:
                    self.dimensions = int(self.dimensions.get())
              except:
                    pass

        for i in range(0,self.width,int(self.width/self.dimensions)):
              self.w.create_line(i,0,i,self.height)
              self.w.create_line(0,i,self.width,i)

   
        print(self.dimensions)
        if len(self.grid) < self.dimensions:
              for i in range(self.dimensions):
                    self.grid.append([])
                    for k in range(self.dimensions):
                          self.grid[i].append(255)

              for i in range(self.dimensions):
                    print(self.grid[i])
        

        self.w.bind('<Button-1>',self.mouse_down)
        self.w.bind('<Motion>',self.motion)

        self.gridWindow.mainloop()

    def mouse_down(self,event):
        try:
              self.x = int(self.xCords[len(self.xCords)-1])
              self.y = int(self.yCords[len(self.yCords)-1])
              self.x = int(self.x/(self.width/self.dimensions))
              self.y = int(self.y/(self.height/self.dimensions))
              self.cord_fill()
        except:
              pass
        
        del self.xCords[:],self.yCords[:]

    def cord_fill(self):
        self.blockWidth = self.width/self.dimensions
        self.w.create_rectangle(self.x*self.blockWidth,self.y*self.blockWidth,(self.x*self.blockWidth)+self.blockWidth,(self.y*self.blockWidth)+self.blockWidth,fill='black')
        #print(self.x*self.blockWidth,self.y*self.blockWidth,(self.x*self.blockWidth)+self.blockWidth,(self.y*self.blockWidth)+self.blockWidth)
        self.grid[self.y][self.x] = 0
        self.w.update()
            
    def motion(self,event):
        self.xCords.append(event.x)
        self.yCords.append(event.y)

grid = []

c = Panel(grid)
c.control()
c.makeGrid()


config = {
    'size': c.dimensions,
    'figsize': (10, 10),
    'grid': c.grid,
}

test = GOL(**config)
test.run()
