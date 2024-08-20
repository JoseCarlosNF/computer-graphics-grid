from algorithms.base import BaseAlgorithm

# Métodos de preenchimento de poligonos.
#
# 1. método de encontrar a `boarda`
#   1.1 para poligonos complexos, não é possível apenas identificar apenas pela
#     borda.
#
# 2. Outra forma de realizar o preenchimento é atráves do `teste de encontro de
#    arestas`.
#    2.1 a cada duas intersecções, uma reta deve ser pintada.
#    2.2 quando a reta passar no vertice, contar duas vezes, uma de cada reta.
#    2.3 como auxilio, podemos ter uma tabela de apoio para identificar quais
#      lados do poligono está sendo tocado para linha de rasterização atual.
#
# 3. Outro método de realizar o preenchimento e atráves do `teste de paridade`
#    (prx. aula dia 2024-08-15).
#    3.1 um algoritmo recursivo, que identifica dentre os pixels adjacentes qual
#      tem a mesma cor do pixel de origem do preenchimento, semelhante ao que
#      acontece com a ferramenta de balde do paint.
#   3.2 foto tirada no dia 13-08-2024 com o algoritmo recursivo de
#     preenchimento.


class Fill(BaseAlgorithm):
    def run(self, selected_cells, rendered_cells, parameters):
        points_to_fill = self.__edge_fill(rendered_cells)

        for cell in points_to_fill:
            self.grid.render_cell(cell)


    def __edge_fill(self, points):
        """
        Preenche o interior do polígono definido pelos pontos utilizando a técnica de teste de encontro de arestas.
        """
        if not points:
            return []

        # Encontre os limites do polígono
        x_min = min(x for x, y in points)
        x_max = max(x for x, y in points)
        y_min = min(y for x, y in points)
        y_max = max(y for x, y in points)

        filled_points = []

        # Varre linha por linha no intervalo de y
        for y in range(y_min, y_max + 1):
            # Encontra os pontos de interseção com a linha de varredura
            intersections = []
            for i in range(len(points)):
                x1, y1 = points[i]
                x2, y2 = points[(i + 1) % len(points)]
                
                # Verifica se a linha (x1, y1) -> (x2, y2) cruza a linha de varredura
                if (y1 <= y < y2) or (y2 <= y < y1):
                    x_intersect = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                    intersections.append(int(x_intersect))

            # Ordena os pontos de interseção
            intersections.sort()

            # Preenche entre os pares de interseção
            for i in range(0, len(intersections), 2):
                if i + 1 < len(intersections):
                    for x in range(intersections[i], intersections[i + 1] + 1):
                        filled_points.append((x, y))

        return filled_points
