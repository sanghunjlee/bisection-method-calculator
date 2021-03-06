"""This module contains iteration method(s) that is used to find the zero.

BisectionMethod will calculate the zero by using the bisection method -- the next subdivision is found using an average of the previous subdivision's endpoints.
"""

import logging
from random import uniform
from mathform import MathFormula

MARGIN_OF_ERROR = 0.000000001


class BisectionMethod(object):
    """Method used for finding zero via bisecting existing subdivision.
    
    Keyword arguments:
    _f -- math-formula.MathFunction object, that is, the function for which the zero is calculated

    """
    _f: MathFormula
    is_single_variable: bool

    def __init__(self, math_formula):
        self._f = math_formula
        self.is_single_variable = (len(self._f.variables) == 1)

    def find_zero(self, a=None, b=None) -> float:
        """

        Args:
            a: start-point of the subdomain of the function on which to find the zero (default: None)
            b: endpoint of the subdomain of the function on which to find the zero (default: None)


        Returns:

        """
        if self.is_single_variable:
            interval = [-1.0, 1.0]
            unbounded = True
            if a is not None and b is not None:
                unbounded = False
                interval = [a, b]
            var = self._f.variables[0]
            variable_value_dict = {var: 0.0}
            points = []

            while len(points) < 2:
                x = uniform(interval[0], interval[1])
                variable_value_dict[var] = x

                try:
                    y = self._f.evaluate(**variable_value_dict)
                except ValueError:
                    raise ValueError('Cannot establish the starting interval')
                print(f"for x = {x}, f(x) = {y}")

                if len(points) == 0:
                    points.append((x, y))
                elif y * points[0][1] < 0:
                    points.append((x, y))
                else:
                    if unbounded:
                        interval[0] = interval[0] - (interval[1] - interval[0])
                        interval[1] = interval[1] + (interval[1] - interval[0])

            for i in range(50):
                x_b = (points[0][0] + points[1][0]) / 2
                variable_value_dict[var] = x_b
                try:
                    y_b = self._f.evaluate(**variable_value_dict)
                except ValueError:
                    raise ValueError(f'Cannot evaluate such value: {x_b}')
                if y_b == 0 or abs(y_b) < MARGIN_OF_ERROR:
                    break
                elif y_b * points[0][1] < 0:
                    points[1] = (x_b, y_b)
                elif y_b * points[1][1] < 0:
                    points[0] = (x_b, y_b)
                print(f"{i}\t|{x_b:.10f}\t|{y_b}\t\t")

            logging.info(f"The zero of the function is: {x_b:.8}")
            return x_b
