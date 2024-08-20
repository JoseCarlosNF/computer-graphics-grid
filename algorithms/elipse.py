from algorithms.base import BaseAlgorithm


class Elipse(BaseAlgorithm):
    def run(self, selected_cells, rendered_cells, parameters):

        rx = int(parameters['Rx'])
        ry = int(parameters['Ry'])
        cx = int(parameters['Cx'])
        cy = int(parameters['Cy'])

        self.__middle_point_elipse(rx, ry, cx, cy)

        for cell in self.points:
            self.grid.render_cell(cell)

    def __plot_point(self, x_center, y_center, x, y, points):
        """
        Adiciona os pontos da elipse nas quatro regiões simétricas.
        """
        points.append((x_center + x, y_center + y))
        points.append((x_center - x, y_center + y))
        points.append((x_center + x, y_center - y))
        points.append((x_center - x, y_center - y))

    def __middle_point_elipse(self, rx, ry, xc, yc):
        """
        Retorna os pontos necessários para rasterizar uma elipse utilizando o algoritmo do ponto médio.
        """
        self.points = []

        # Região 1
        x = 0
        y = ry
        p1 = (ry**2) - (rx**2 * ry) + (0.25 * rx**2)
        dx = 2 * ry**2 * x
        dy = 2 * rx**2 * y

        # Plotando os pontos iniciais
        self.__plot_point(xc, yc, x, y, self.points)

        # Enquanto o gradiente da elipse for < -1
        while dx < dy:
            x += 1
            dx += 2 * ry**2
            if p1 < 0:
                p1 += dx + ry**2
            else:
                y -= 1
                dy -= 2 * rx**2
                p1 += dx - dy + ry**2
            self.__plot_point(xc, yc, x, y, self.points)

        # Região 2
        p2 = (ry**2) * ((x + 0.5)**2) + (rx**2) * ((y - 1)**2) - (rx**2 * ry**2)

        while y > 0:
            y -= 1
            dy -= 2 * rx**2
            if p2 > 0:
                p2 += rx**2 - dy
            else:
                x += 1
                dx += 2 * ry**2
                p2 += dx - dy + rx**2
            self.__plot_point(xc, yc, x, y, self.points)
