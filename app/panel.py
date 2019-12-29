from tkinter import *


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
