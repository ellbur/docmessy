#!/usr/bin/python

from docmessy import sur

@sur('<html>', '</html>')
def _():
    @sur('<head>', '</head>')
    def _():
        print('<title>Hello, World!</title>')
        
    @sur('<body>', '</body>')
    def _():
        @sur('<p>', '</p>')
        def _():
            print('Hello, World!')


