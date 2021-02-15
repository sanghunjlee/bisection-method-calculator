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
    logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%H:%M:%S')
    start_time = time.time()
    logging.info('LOG START: ' + datetime.now().strftime('%Y/%m/%d'))

    user_input = input('Input the function: ')
    f = MathFormula(user_input)
    bm = BisectionMethod(f)
    z = bm.find_zero()
    print(z)

    end_time = time.time()
    logging.info(f'LOG END: RUNTIME = {end_time - start_time}')


if __name__ == "__main__":
    main()