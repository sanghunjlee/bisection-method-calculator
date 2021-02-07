"""This is the main module.

This module takes in the user input, runs it through the math-formula class, and finally feeds it to the iter-calc.BisectionMethod.
"""

__version__ = '0.1'
__author__ = 'Sanghun Joseph Lee'

from mathform import MathFormula
from itercalc import BisectionMethod

def main():
    user_input = input('Input the function: ')
    f = MathFormula(user_input)
    BisectionMethod(f, a=0, b=1)

if __name__ == "__main__":
    main()
