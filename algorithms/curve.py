from algorithms.base import BaseAlgorithm


class BezierCurve(BaseAlgorithm):
    """
    Implementa uma curva de Bezier cúbica, com quatro pontos de ancoragem.
    """

    # TODO:
    # - [ ] funções polinomiais paramétricas
    # - [ ] funções de base de bezier

    def run(self, selected_cells, rendered_cells, parameters):
        points = self.calculate_bezier_curve(selected_cells, 3)
        breakpoint()

    def calculate_bezier_curve(self, points, num_points):
        n = len(points) - 1
        t_increment = 1 / num_points

        coordinates = []

        for i in range(num_points + 1):
            t = i * t_increment
            x, y = 0, 0

            for j in range(n + 1):
                coefficient = (
                    self.binomial_coefficient(n, j)
                    * (1 - t) ** (n - j)
                    * t**j
                )
                x += coefficient * points[j][0]
                y += coefficient * points[j][1]

            coordinates.append((int(x), int(y)))

        return coordinates

    def binomial_coefficient(self, n, k):
        coefficient = 1

        for i in range(k):
            coefficient *= n - i
            coefficient //= i + 1

        return coefficient

    def bezier(self, src_point: tuple, dest_point: tuple):
        """
        Calcula uma curva de bezier.

        Parameters:
            src_point (tuple):

            dest_point (tuple):

        Returns:
            points (list):
        """

        points = []
        return points
