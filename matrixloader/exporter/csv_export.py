import csv

class CSVEdgeListExport():
    def __init__(self, output, headers=False):
        self._sources  = []
        self._dests    = []
        self._values   = []
        self._file = output
        self._headers = headers

    def add_edge(self, row, column, value):
        self._sources.append(row)
        self._dests.append(column)
        self._values.append(value)
        
    def reserve(self, rows, columns, nonzeros):
        pass

    def build(self):
        writer = csv.writer(self._file)
        if self._headers is not None:
            writer = csv.writer(self._file)
            writer.writerow(self._headers)
        writer.writerows(zip(self._sources,self._dests,self._values))
