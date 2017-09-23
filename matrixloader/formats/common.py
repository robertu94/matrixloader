"""
This module provides common functions for building Format Parsers
"""
def ignore_comments(func):
    def wrap(self, line):
        if line.startswith('%'):
            return
        func(self, line)
    return wrap

