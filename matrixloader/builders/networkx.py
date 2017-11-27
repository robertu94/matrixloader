from networkx import DiGraph

class NetworkXBuilder():
    def __init__(self, matrix_function=None):
        self._matrix_function = matrix_function or DiGraph
        self._graph = self._matrix_function()
        self._edges = []
    def add_edge(self, row, column, value):
        self._edges.append((row, column, {"weight":value}))
    def reserve(self, rows, columns, nonzeros):
        """networkx graphs are stored as dicts and don't support reserving"""
        pass
    def build(self):
        self._graph.add_edges_from(self._edges)
        return self._graph
