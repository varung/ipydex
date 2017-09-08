# -*- coding: utf8 -*-


import numpy as np
from numpy import sin, cos


from ipydex import IPS, ip_syshook, ST

"""
This example shows how the tools from module ipydex may be used.
"""


ip_syshook(1) # enable debugger on exception



def func1(q):
    return cos(q) + 5


def func2(q1, q2):
    """
    to demonstrate debugging on exception
    """

    a = q1/q2
    
    if q2 == 5:
        z = 7
        IPS() # start embedded ipython shell in the local scope
        # -> explore global namespace

    
    return a



# ST() # start tracicing start command line debugger here
# presse h <Enter> for help
# n <Enter> to execute next line
# q <Enter> to quit


x = np.linspace(0, 20, 100)

y = sin(x)

z = func1(x) - 5

u = y**2 + z**2# should be an array full of 1.0


b1 = func2(1.0, 2.0)
b2 = func2(1.0, 5)  # start IPS inside func2


#b2 = func2(1.0, 0)  # ZeroDivisionError -> start interactive debugger


#IPS() # start embedded ipython shell on top level scope
# -> explore global namespace

