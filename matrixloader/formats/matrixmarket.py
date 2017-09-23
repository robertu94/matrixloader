"""This module defines a parser for the matrix market format"""
from .common import ignore_comments

class MatrixMarketParser():
    def _header_state(self, line):
        magic, self.obj, self.format, \
            self.field, self.symmetry = line.split()
        size_states = {
            "coordinate": self._coordinate_size_state,
            "array": self._array_size_state,
        }
        self._state = size_states[self.format]

    @ignore_comments
    def _coordinate_size_state(self,line):
        self._state = self._coordinate_data_state
        rows, columns, nonzeros = map(int, line.split())
        self._builder.reserve(rows,columns,nonzeros)

    @ignore_comments
    def _coordinate_data_state(self,line):
        split = line.split()
        if self.field != "pattern":
            self._builder.add_edge(int(split[0])-1,
                                  int(split[1])-1,
                                  self._value_fn(split[2]))
        else:
            self._builder.add_edge(int(split[0])-1,
                                  int(split[1])-1,
                                  self._default_value)
    
    @ignore_comments
    def _array_size_state(self,line):
        rows, columns = map(int, line.split())
        self._builder.reserve(rows, columns, rows*columns)
        self._state = self._array_data_state
        self._row = 0
        self._column = 0

    @ignore_comments
    def _array_data_state(self,line):
        self._builder.add_edge(self._row,
                                self._column,
                                self._value_fn(line))
        #TODO there is probably some clever way to do this with generators
        self._row += 1
        if self._row == rows:
            self._column += 1
            self._row = 0
        

    def __init__(self, builder, value_fn=float, default_value="1"):
        self._builder = builder
        self._state   = self._header_state
        self._value_fn = value_fn
        self._default_value = value_fn(default_value)

    def parse(self, matfile):
        for line in matfile:
            self._state(line)
        return self._builder.build()
