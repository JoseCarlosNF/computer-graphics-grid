from grid import Grid
from libs.logger import log


class BaseAlgorithm:
    """
    Classe utilizada como base para para construir as classes dos algoritmos.

    A partir dela temos alguns mecanismos que podem ajudar em troubleshootings e
    apoiar a tipagem, para facilitar o autocomplete em editores com
    suporte.
    """

    def __init__(self, grid: Grid, debug: bool = False) -> None:
        self.grid = grid
        self.debug = debug
        self.log = log(self.__class__.__name__)

    def run(self, selected_cells, rendered_cells, parameters):
        """
        TODA CLASSES CRIADA A PARTIR DESSA, deve ter esse método.

        Nele estará o código principal. Tudo o que for colocado dentro desse
        método será executado sempre que a classe for chamada.
        """
        pass

    def __call__(self, selected_cells, rendered_cells, parameters):
        self.run(selected_cells, rendered_cells, parameters)
        if self.debug:
            self.log.debug(f'selected_cells: {selected_cells}')
            self.log.debug(f'rendered_cells: {rendered_cells}')
            self.log.debug(f'parameters: {parameters}')
