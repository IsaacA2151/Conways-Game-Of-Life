import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class GOL:
    def __init__(self):
        pass
    
    def randomGrid(self):
        self.grid = np.random.choice([0,255],10*10,p=[0.9,0.1]).reshape(10,10)  # Creates a random 4*4 grid with 0 or 255 value, 
        #0 being off and 255 being on, p is probability off either colour
        
        plt.imshow(self.grid)  # Displays
        
    def update(self):
        pass

    def applyRules(self):
        pass
    
test = GOL()
test.randomGrid()
print(test.grid)