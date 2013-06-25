#!/usr/bin/python

from docmessy import sur, pyplot_image
from matplotlib.pyplot import *
from numpy import *
from cgi import escape

x = random.normal(size=50)
y = random.normal(size=50)

@sur('<html>', '</html>')
def _():
    print('<head><title>Example of plotting</title></head>')
    @sur('<body>', '</body>')
    def _():
        @sur('<p>', '</p>')
        def _():
            print('''
                Here we show an example of producing a plot using docmessy.
                
                The plot is embedded as a
                <a href="https://en.wikipedia.org/wiki/Data_URI_scheme">data URI</a>
                so that we get a standalone document that we could email to someone.
            ''')
        
        @pyplot_image()
        def _():
            plot(x, y, 'o')
            xlabel('x')
            ylabel('y')


