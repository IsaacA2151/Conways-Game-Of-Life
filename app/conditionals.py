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
