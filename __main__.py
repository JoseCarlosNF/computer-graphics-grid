from algorithms.bresenham import Bresenham
from algorithms.circle import Circle
from algorithms.elipse import Elipse
from algorithms.fill import Fill
from algorithms.paint import Paint
from grid import Grid

grid = Grid(10, 600)

grid.add_algorithm('Bresenham', algorithm=Bresenham(grid))
grid.add_algorithm('Circulo', algorithm=Circle(grid), parameters=['Raio'])
grid.add_algorithm('Paint', algorithm=Paint(grid))
grid.add_algorithm('Elipse', algorithm=Elipse(grid), parameters=['Rx','Ry','Cx','Cy'])
grid.add_algorithm('Preenchimento', algorithm=Fill(grid))

grid.show()
