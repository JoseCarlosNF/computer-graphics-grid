from algorithms.base import BaseAlgorithm


class Bresenham(BaseAlgorithm):
    """
    Gerar os pontos necessários para traçar um reta entre os dois pontos
    selecionados.
    """

    def __get_angle(self, p_1=(int, int), p_2=(int, int)) -> float:
        """
        Obtem o coeficiente angular da reta.

        Tem precisão de 2 CASAS DECIMAIS.
        """
        return round((p_2[1] - p_1[1]) / (p_2[0] - p_1[0]), 2)

    def __get_points(
        self, p_1=(int, int), p_2=(int, int)
    ) -> list[tuple[int, int]]:
        """
        Obtem os pontos gerados.
        """
        m = self.__get_angle(p_1, p_2)
        self.log.info(f'para p_1={p_1} e p_2={p_2} M é: {m}')
        return [(x, round(m * x)) for x in range(p_1[0], p_2[0] + 1)]

    def run(self, selected_cells, rendered_cells, parameters):
        for cell in self.__get_points(selected_cells[0], selected_cells[1]):
            self.grid.render_cell(cell)
