"""This module contains iteration method(s) that is used to find the zero.

BisectionMethod will calculate the zero by using the bisection method -- the next subdivision is found using an average of the previous subdivision's endpoints.
"""

from math import *


class BisectionMethod(object):
    """Method used for finding zero via bisecting existing subdivision.
    
    Keyword arguments:
    MF_function -- math-formula.MathFunction object, that is, the function for which the zero is calulated
    a -- startpoint of the subdomain of the function on which to find the zero (default 0.0)
    b -- endpoint of the subdomain of the function on which to find the zero (default 1.0)
    """
    MF_f: MathFormula
    def __init__(self, MF_function, a=0.0, b=1.0):
        
