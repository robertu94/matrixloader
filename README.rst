Matrixloader
================================================================================


This library provides an adapter across various graph libraries such as
networkx, networkit or numpy that is used to load matrices of various formats
such as the MatrixMarket format.

Getting started as as simple as::

    from matrixloader import NetworkXBuilder, load
    matrix = load(args.infile, NetworkXBuilder())

Builders
--------------------------------------------------------------------------------

Builders are the adapter for batch building networks/matrices. They provide 4 methods::

    add_edge(self, row: int, column: int, value: Any) -> None:

Add an edge to the network from row to column with weight value. Depending on the builder, the parameter value MAY be ignored. The parser SHOULD call this method one or more times.::

    reserve(self, rows: int, columns: int, nonzeros: int) -> None:

Provide a hint to the implementation as to the number of rows, columns, and nonzeros that will be provided via reserve.  The implementation MAY ignore this call.  The parser MAY call this method at any time.  Calling this function mutliple times MAY result in undefined behavior.::

    build(self) -> Any:

Instruct the builder to return an object. Calling this method more than once on the same object MAY result in undefined behavior.::

Formats
--------------------------------------------------------------------------------

Formats provide a generic implementation of each format implanted in terms of the `Builder` interface.  It provides two methods::

    __init__(self, builder, **kwargs)

The constructor MUST accept a builder as the first argument.  It may accept other keyword arguments.  The provided builder MUST be used to construct the Graph.

    parse(self, infile: TextIO) -> Any

Parses the infile and returns the result of the builder object.


