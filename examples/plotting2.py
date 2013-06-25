#!/usr/bin/python

from docmessy import sur, pyplot_image
from matplotlib.pyplot import *
from numpy import *
from cgi import escape

x = random.normal(size=50)
y = random.normal(size=50)

variables = [
    ('u', x + y),
    ('v', x - y),
    ('w', x * y)
]

@sur('<html>', '</html>')
def _():
    @sur('<head>', '</head>')
    def _():
        print('<title>Example of plotting</title>')

    @sur('<body>', '</body>')
    def _():
        @sur('<table>', '</table>')
        def _():
            @sur('<tr>', '</tr>')
            def _():
                print('<td></td>')
                for name, _ in variables:
                    print('<th>%s</th>' % (escape(name),))
                
            for i in range(len(variables)):
                @sur('<tr>', '</tr>')
                def _():
                    name1, data1 = variables[i]
                    print('<th>%s</th>' % (escape(name1),))
                    
                    for j in range(len(variables)):
                        name2, data2 = variables[j]
                        @sur('<td>', '</td>')
                        def _():
                            @pyplot_image(figsize=(2,2))
                            def _():
                                plot(data2, data1, 'o')
                                xlim(min(data2), max(data2))
                                ylim(min(data1), max(data1))


