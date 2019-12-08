import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class GOL:
    def __init__(self):
        pass
    
    def randomGrid(self):
        self.x = np.random.choice([0,255],4*4,p=[0.5,0.5]).reshape(4,4)  # Creates a random 4*4 grid with 0 or 255 value, 
        #0 being off and 255 being on, p is probabiliy or either colour
        
        plt.imshow(self.x)  # Displays
        
    def update(self):
        pass

    def applyRules(self):
        pass
    
test = GOL()
test.randomGrid()
print(test.x)