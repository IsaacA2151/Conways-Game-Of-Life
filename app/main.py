from gol import *
from panel import *


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
