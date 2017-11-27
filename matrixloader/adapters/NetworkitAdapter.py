class NetworkitAdapter:
    def __init__(self, builder):
        self._builder = builder
    def convert(self, graph):
        rows = columns = graph.numberOfNodes()
        nonzeros = graph.numberOfEdges()
        self._builder.reserve(rows, columns, nonzeros)
        for source,dest in graph.edges():
            weight = graph.weight(source, dest)
            self._builder.add_edge(source, dest, weight)
        return self._builder.build()
