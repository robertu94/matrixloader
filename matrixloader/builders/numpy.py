import scipy.sparse
import numpy as np

class NumPyBuilder():
    def __init__(self, matrix_function=None):
        self._sources  = []
        self._dests    = []
        self._values   = []

        self._reserved = False
        self.rows = None
        self.columns = None

        self._matrix_function = matrix_function or scipy.sparse.csr_matrix

    def add_edge(self, row, column, value):
        self._sources.append(row)
        self._dests.append(column)
        self._values.append(value)
        
    def reserve(self, rows, columns, nonzeros):
        self._reserved = True
        self.rows = rows
        self.columns = columns

    def build(self):
        rows = np.array(self._sources)
        cols = np.array(self._dests)
        data = np.array(self._values)
        if self._reserved:
            return self._matrix_function((data,(rows,cols)), shape=(self.rows, self.columns))
        return self._matrix_function((data,(rows,cols)))

