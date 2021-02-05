"""This is the main module.

This module takes in the user input, runs it through the math-formula class, and finally feeds it to the iter-calc.BisectionMethod.
"""

__version__ = '0.1'
__author__ = 'Sanghun Joseph Lee'

from iter-calc import BisectionMethod
from math-formula import MathFormula


def main():
    user_input = input('Input the function: ')
    MF_function = MathFormula(user_input)
    BisectionMethod(MF_function, a=0, b=1)

if __name__ == "__main__":
    main()
