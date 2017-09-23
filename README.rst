Matrixloader
================================================================================


This library provides an adapter across various graph libraries such as networkx or numpy
that is used to load matrices of various formats such as the matrixmarket format.

Getting started as as simple as:

::
    from matrixloader import MatrixMarketParser, NetworkXBuilder, load

    matrix_parser = MatrixMarketParser(NetworkXBuilder())
    matrix = load(args.infile, matrix_parser)


