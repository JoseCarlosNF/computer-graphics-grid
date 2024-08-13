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
        return super().run(selected_cells, rendered_cells, parameters)
