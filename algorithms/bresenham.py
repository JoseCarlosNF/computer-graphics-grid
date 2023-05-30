from algorithms.base import BaseAlgorithm


class Bresenham(BaseAlgorithm):
    """
    Gerar os pontos necessários para traçar um reta entre os dois pontos
    selecionados.

    Foi implementada uma versão que utiliza a detecção de diferença entre os
    pontos para identificar seu vetor, de maneira que possa ser aplicavel em
    qualquer quadrante, independente do coeficiente angular entre os pontos.

    Em resumo, a utilização do coeficiente angular, foi substituida pela
    avaliação de diferença entre os pontos. Essa abordagem foi escolhida por se
    tratar de um ambiente controlado, cujos pontos serão sempre inteiros.
    """

    def __get_points(self, p_1, p_2) -> list[tuple[int, int]]:
        points = []
        x1, y1 = p_1
        x2, y2 = p_2

        # DIFERENÇA DE PIXELS ENTRE OS PONTOS.
        # Útil para identificar a quantidade de pixels que precisaram ser
        # percorridos em cada eixo.
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        # DETECTA A DIREAÇÃO DA RETA.
        # Atráves da diferença entre os pontos. Se x1 > x2, quer dizer que a
        # linha está indo para a esquerda, logo o x será decrementado a cada
        # interação. Analogamente essa definição é aplicada no eixo y.
        sx = -1 if x1 > x2 else 1
        sy = -1 if y1 > y2 else 1

        # ERRO ACUMULADO (distância até o ponto médio mais próximo)
        # Útil para decidir qual será o próximo pixel a ser pintado.
        err = dx - dy

        # Substituição do nome das variaveis para facilitar a leitura do loop
        x, y = x1, y1

        # Pecorrer os pontos
        # Sai de p_1 e vai até p_2
        while x != x2 or y != y2:
            # de cara adiciona o primeiro ponto.
            # Posteriormente, com as substituições, os demais pontos são gerados.
            points.append((x, y))
            e2 = 2 * err

            # Incrementa/Decrementa no eixo X
            if e2 > -dy:
                err -= dy
                x += sx

            # Incrementa/Decrementa no eixo Y
            if e2 < dx:
                err += dx
                y += sy

        # Adiciona o último ponto a lista de pontos para a rasterização da linha
        points.append((x, y))
        return points

    def run(self, selected_cells, rendered_cells, parameters):
        # Validação da quantidade de pontos selecionados
        if not len(selected_cells) == 2:
            self.log.error(
                'O número de pontos selecionados deve ser igual a 2'
            )
            return 1

        # Obtenção dos pontos
        points = self.__get_points(selected_cells[0], selected_cells[1])
        self.log.info(f'Pontos obtidos {points}')

        # Rasterização dos pontos selecionados
        for cell in points:
            if self.debug:
                self.log.debug(f'Pintando ponto {cell}')
            self.grid.render_cell(cell)
