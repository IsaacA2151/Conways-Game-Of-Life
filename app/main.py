import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

size = 10

class GOL:
    def __init__(self):
        self.surrounding = 0  # Keeps track of surrouding alive cells
    
    def randomGrid(self):
        self.grid = np.random.choice([0,255],size*size,p=[0.1,0.9]).reshape(size,size)  # Creates a random size*size grid with 0 or 255 value, 
        # 0 being off and 255 being on, p is probability off either colour
        
        plt.imshow(self.grid)  # Displays
        
    def update(self):
        pass

    def applyRules(self):
        pass
    
    def checkRules(self):
        print(self.grid)
        for i in range(len(self.grid)):
            for k in range(len(self.grid)):
                self.surrounding = 0
                
                checkCon = Conditionals(self.grid,i,k)
                checkCon.find()
                
                '''if checkCon.N:
                    if self.grid[i-1][k] == 0:
                        self.surrounding += 1
                        
                if checkCon.E:
                    if self.grid[i][k+1] == 0:
                        self.surrounding += 1
                        
                if checkCon.S:
                    if self.grid[i+1][k] == 0:
                        self.surrounding += 1
                        
                if checkCon.W:
                    if self.grid[i][k-1] == 0:
                        self.surrounding += 1
                        
                if checkCon.NE:
                    if self.grid[i-1][k+1] == 0:
                        self.surrounding += 1
                        
                if checkCon.SE:
                    if self.grid[i+1][i+1] == 0:
                        self.surrounding += 1
                
                if checkCon.SW:
                    if self.grid[i+1][k-1] == 0:
                        self.surrounding += 1
                
                if checkCon.NW:
                    if self.grid[i-1][k-1] == 0:
                        self.surrounding += 1            

                print(i,k,self.surrounding)'''

class Conditionals:
    
    def __init__(self,grid,y,x):
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
        # These just check which directoins are possible without causing the index to go out of range
        if self.y != 0:
            self.N = True
            
        if self.x != len(self.grid):
            self.E = True
        
        if self.y != len(self.grid):
            self.S = True
        
        if self.x != 0:
            self.W = True
            
        if self.y != 0 and self.x != len(self.grid):
            self. NE = True
            
        if self.y != len(self.grid) and self.x != len(self.grid):
            self.SE = True
            
        if self.y != len(self.grid) and self.x != 0:
            self.SW = True
            
        if self.y != 0 and self.x != 0:
            self.NW = True
        

test = GOL()
test.randomGrid()
test.checkRules()
print(test.grid)
