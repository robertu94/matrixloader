class NetworkXAdapter:
    def __init__(self, builder):
        self._builder = builder

    def convert(self, graph):
        rows, cols = graph.number_of_nodes()
        nonzeros = graph.number_of_edges()
        self._builder.reserve(rows, cols, nonzeros)
        for row, col, value in graph.edges.data('weight'):
            value = value or 1
            self._builder.add_edge(row, col, value)
        return self._builder.build()
