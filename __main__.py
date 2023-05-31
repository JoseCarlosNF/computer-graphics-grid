from algorithms.bresenham import Bresenham
from algorithms.circle import Circle
from algorithms.paint import Paint
from grid import Grid

grid = Grid(10, 600)

grid.add_algorithm('Bresenham', algorithm=Bresenham(grid))
grid.add_algorithm('Circulo', algorithm=Circle(grid), parameters=['Raio'])
grid.add_algorithm('Paint', algorithm=Paint(grid))

grid.show()
