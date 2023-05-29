from algorithms.bresenham import Bresenham
from algorithms.paint import Paint
from grid import Grid

grid = Grid(10, 600)

grid.add_algorithm('Bresenham', algorithm=Bresenham(grid, True))
grid.add_algorithm('Paint', algorithm=Paint(grid, True))

grid.show()
