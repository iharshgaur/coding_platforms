import textwrap

def wrap(string, max_width):
    for i in textwrap.wrap(string,max_width):
        print(i)
    
string='ABCDEFGHIJKLIMNOQRSTUVWXYZ'
max_width=4
wrap(string, max_width)