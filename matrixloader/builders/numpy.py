import scipy.sparse
import numpy as np

class NumPyBuilder():
    def __init__(self, matrix_function=None):
        self.sources  = []
        self.dests    = []
        self.values   = []

        self.reserved = False
        self.rows = None
        self.columns = None

        self.matrix_function = matrix_function or scipy.sparse.csr_matrix

    def add_edge(self, row, column, value):
        self.sources.append(row)
        self.dests.append(column)
        self.values.append(value)
        
    def reserve(self, rows, columns, nonzeros):
        self.reserved = True
        self.rows = rows
        self.columns = columns

    def build(self):
        rows = np.array(self.sources)
        cols = np.array(self.dests)
        data = np.array(self.values)
        if self.reserved:
            return self.matrix_function((data,(rows,cols)), shape=(self.rows, self.columns))
        return self.matrix_function((data,(rows,cols)))

