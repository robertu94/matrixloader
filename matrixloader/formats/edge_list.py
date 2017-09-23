"""implements a parser for a naive edge list format"""
from .common import ignore_comments

class EdgeListParser():
    def __init__(self, builder, value_fn=float, zero_indexed=True, default_value="1"):
        self._builder = builder
        self.value_fn = value_fn
        self.node_fn = int if zero_indexed else lambda x: int(x)-1
        self.default_value = value_fn(default_value)

    @ignore_comments
    def _parse(self, line):
        split= line.split()
        source = split[0]
        dest = split[1]
        try:
            value = split[2]
        except IndexError:
            value = self.default_value
        self._builder.add_edge(self.node_fn(source),
                              self.node_fn(dest),
                              self.value_fn(value))
    def parse(self, matfile):
        for line in matfile:
            self._parse(line)
        return self._builder.build()
