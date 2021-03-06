
from quickfiles import *
from base64 import b64encode

def surround_with(start, end):
    '''A decorator to run a block of code,
       preceded by printing `start` and followed by
       printing `end`.
       
       Example usage::
           
           @surround_with('<p>', '</p>')
           def _():
               print('Hello, paragraph.')
           
       An abbreviation `sur` = `surround_with` exists in this module.
           
       '''
       
    def dec(f):
        print(start)
        f()
        print(end)
        
    return dec

sur = surround_with

def pyplot_image(**fig_attrs):
    '''A decorator to embed a plot as an <img/> with a data-URI.
    
       Arguments are passed to figure().
       
       Result (as with everything in docmessy) is printed using print(),
       ie to stdout.
       
       Example:
           
           @pyplot_image(figsize=(2,2))
           def _():
               plot(range(5), range(5))
               xlabel('x')
               ylabel('y')
    '''
    
    from matplotlib.pyplot import figure
    
    def dec(f):
        fig = figure(**fig_attrs)
        f()
        tmp = Path.mktemp().setext('.png')
        fig.savefig(str(tmp))
        data = b64encode(open(str(tmp)).read())
        print('<img src="data:image/png;base64,%s"/>' % (data,))
    return dec

