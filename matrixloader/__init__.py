"""
This library offers parsers and builders for various matrix formats
Copyright © 2017 Robert Underwood
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY Robert Underwood ''AS IS'' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL Robert Underwood BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation
are those of the authors and should not be interpreted as representing
official policies, either expressed or implied, of Robert Underwood.
"""

import matrixloader.formats
from matrixloader.formats import *
import matrixloader.builders
from matrixloader.builders import *
import matrixloader.exporter
from matrixloader.exporter import *


def load(infile, builder, default_parser=None):
    """
    load file and guess the parser based on the extension

    Args:
       infile (typing.TextIO): the graph file to parse
       builder (matrixloader.Builder): the builder for the type to return
       default_parser (typing.Callable[[matrixloader.Builder], matrixloader.Parser]: if the type is not found use this one

    Returns:
        graph (typing.Any): the graph constructed by builder
    """
    formats = {
        "mtx": MatrixMarketParser
    }
    default_parser = default_parser or (lambda builder: EdgeListParser(builder, zero_indexed=False))
    extension = infile.name.split('.')[-1]
    constructor = formats.get(extension, default_parser)
    return constructor(builder).parse(infile)
