"""This module contains a class for interpreting user inputted math formula.

MathFormula first checks if the input can be understood, and evaluates given a value.
"""

__all__ = ['MathFormula']

import logging
from math import pow


class Operator:
    parenthesis_start = '('
    parenthesis_end = ')'
    exponential = '^'
    multiplication = '*'
    division = '/'
    addition = '+'
    subtraction = '-'
    all = ['(', ')', '^', '*', '/', '+', '-']


class MathFormula(object):
    formula: str
    variables: [str]
    order_of_operations: [str]

    def __init__(self, user_input):
        self.formula = user_input
        self._simplify_formula()

    def _simplify_formula(self):
        """This function will simplify _formula by doing the following 2 things:

        1: Remove blank space(s).
        2: Add multiplication operator (*) where it's implied (e.g. 3x^2 ==> 3*x^2)
        """
        eq = self.formula.replace(' ', '')
        result = []

        # Add multiplication operator where it's implied
        for i in range(len(eq)):

            if i != 0 and ((eq[i].isalpha() or eq[i] == "(") and (eq[i-1].isnumeric() or eq[i-1].isalpha())):
                result.append('*')
            result.append(eq[i])
        self.formula = ''.join(result)
        self.formula = self.formula.replace('^', '**')
        logging.info(f'function: {self.formula}')

    def _identify_variable(self):
        """This function will identify the variable and append to _variables.

        Next: identify the greek letters (written in the forms of %pi% or /pi or such)
        """
        self.variables = []
        for c in self.formula:
            if c.isalpha() and c not in self.variables and c not in ['e']:
                self.variables.append(c)
        self.variables.sort()
        logging.info(f'variable(s): {self.variables}')

    def _substitute_value(self, **kwargs):
        """This function will replace variables in _formula with values given in kwargs

        Args:
            **kwargs: variable-value pair(s)

        Returns:
            string of the _formula with each variable replaced with respective value
        """
        result = self.formula
        for _ in self.variables:
            if _ in kwargs.keys():
                result = str(kwargs[_]).join(result.split(_))
            else:
                raise KeyError("The value for the variable " + _ + " not given")
        return result

    def evaluate(self, **kwargs) -> float:
        """This function will calculate the value of the function at given input.

        Args:
            **kwargs: variable-value pair(s)

        Returns: the value of the function with the given value for the variables.
        """
        if len(kwargs.keys()) != len(self.variables):
            raise IndexError("ERROR: values-to-variables mismatch")
        else:
            try:
                answer = eval(self.formula, {}, kwargs)
                return float(answer)
            except SyntaxError:
                raise SyntaxError
            except NameError:
                raise NameError
            except TypeError:
                raise TypeError
