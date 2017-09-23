from networkx import DiGraph

class NetworkXBuilder():
    def __init__(self, matrix_function=None):
        self._matrix_function = matrix_function or DiGraph
        self._graph = self._matrix_function()
    def add_edge(self, row, column, value):
        self._graph.add_edge(row, column, weight=value)
    def reserve(self, rows, columns, nonzeros):
        """networkx graphs are stored as dicts and don't support reserving"""
        pass
    def build(self):
        return self._graph
