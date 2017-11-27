from networkit.graph import Graph

class NetworkitBuilder():
    def __init__(self, graph_fn=None, **kwargs):
        self._graph_fn = graph_fn or Graph
        self._edges = []
        self._rows = None
        self._cols = None
        self._values = None
        self._kwargs = kwargs
        self._max_n = 0
    def __str__(self):
        return "NetworkitBuilder<{kwargs}>".format(kwargs=kwargs)

    def add_edge(self, row, column, value):
        self._max_n = max(self._max_n, row, column)
        self._edges.append((row, column, value))

    def reserve(self, rows, columns, nonzeros):
        """networkit graphs do not support reserving"""
        self._rows = rows
        self._cols = columns
        self._values = nonzeros

    def build(self):
        if self._rows is not None:
            self._graph = self._graph_fn(n=max(self._rows, self._cols), **self._kwargs)
        else:
            self._graph = self._graph_fn(n=self._max_n+1,**self._kwargs)

        for row, col, weight in self._edges:
            self._graph.addEdge(row, col, w=weight)

        return self._graph

