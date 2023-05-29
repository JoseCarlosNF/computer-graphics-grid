from algorithms.base import BaseAlgorithm


class Paint(BaseAlgorithm):
    def run(self, selected_cells, rendered_cells, parameters):
        for cell in selected_cells:
            self.grid.render_cell(cell)
