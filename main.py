"""This is the main module.

This module takes in the user input,
runs it through the math-formula class,
and finally feeds it to the iter-calc.BisectionMethod.
"""

__version__ = '0.1'
__author__ = 'Sanghun Joseph Lee'

import logging
from datetime import datetime
import time
from mathform import MathFormula
from itercalc import BisectionMethod

def main():
    logging.basicConfig(filename='debug.log', level=logging.INFO)
    start_time = time.time()
    logging.info('Log Start: ' + datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

    user_input = input('Input the function: ')
    f = MathFormula(user_input)
    bm = BisectionMethod(f)
    z = bm.find_zero(0.0, 1.0)
    print(z)

    end_time = time.time()
    logging.info(f'Runtime: {end_time - start_time}')
    logging.info('Log End: ' + datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

if __name__ == "__main__":
    main()
