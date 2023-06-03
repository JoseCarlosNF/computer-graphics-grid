from algorithms.base import BaseAlgorithm


class Circle(BaseAlgorithm):
    """
    Partindo dos conhecimentos obtidos com o algoritmo de Bresenham, utilizando
    a técnica do cálculo de erro, os pontos base são calculados e posteriormente
    seus correspondentes em todos os octantes, em relação ao centro, são obtidos
    através do espelhamento de coordenadas.
    """

    def run(self, selected_cells, rendered_cells, parameters):
        if not len(selected_cells) == 1:
            self.log.error(
                'Apenas 1 ponto deve ser selcionado. O centro do circulo.'
            )
            return

        center = selected_cells[-1]
        base_points = self.__get_base_points(int(parameters['Raio']))
        points = self.__get_circle_points(center, base_points)

        for cell in points:
            self.grid.render_cell(cell)

    def __get_base_points(self, radius: int) -> list[tuple[int, int]]:
        """
        Obtem os pontos base, que serão utlizados para gerar os pontos em cada
        uma dos octantes.

        Parameters:
            radius (int): Raio do círculo.

        Returns:
            base_points (list): Uma lista de tuplas, com as coordenadas dos
            pontos base.
        """
        x, y = 0, radius
        err = -radius
        base_points = []

        # Primeiro ponto
        base_points.append((x, y))

        # Calcula os pontos base, utilizando Bresenham
        while x <= y:
            err += 2 * x + 1
            x += 1
            if err >= 0:
                err += 2 - 2 * y
                y -= 1
            base_points.append((x, y))

        self.log.info(f'Pontos base {base_points}')
        return base_points

    def __get_circle_points(
        self, center: tuple, base_points: list[tuple[int, int]]
    ) -> list[tuple[int, int]]:
        """
        A partir de uma lista de coordenadas, dos pontos base, gera seus pontos espelhados nos 8
        octantes. Utiliza o espelhamento entre os octantes.

        Parameters:
            center (tuple): Tupla com as coordenadas do centro do círculo.

            base_points (list): Lista com os pontos que serviram como base para
            geração dos pontos correspondentes nos 8 octantes.

        Returns:
            points (list): Lista de pontos espelhados nos 8 octantes.
        """
        x_c, y_c = center
        points = []

        for point in base_points:
            x, y = point[0], point[1]

            self.log.info(f'Gerando os pontos a partir do ponto base {point}')

            # Espelha os pontos bases em todos os octantes.
            for octant in range(8):
                match octant:
                    case 0:
                        points.append((y + x_c, x + y_c))
                    case 1:
                        points.append((x + x_c, y + y_c))
                    case 2:
                        points.append((-x + x_c, y + y_c))
                    case 3:
                        points.append((-y + x_c, x + y_c))
                    case 4:
                        points.append((-y + x_c, -x + y_c))
                    case 5:
                        points.append((-x + x_c, -y + y_c))
                    case 6:
                        points.append((x + x_c, -y + y_c))
                    case 7:
                        points.append((y + x_c, -x + y_c))
                self.log.info(f'{octant+1}° octante {points[-1]} ')

        if self.debug:
            self.log.debug(f'Pontos encontrados {points}')

        return points
