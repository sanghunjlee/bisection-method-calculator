"""This module contains a class for interpreting user inputted math formula.

MathFormula first checks if the input can be understood, and evaluates given a value.
"""

import logging
from math import pow


def _computation(expression):
    result = expression
    parenthesis = "(" in result
    while parenthesis:
        print("Working on Parenthesis")
        split_ends = result.split("(")
        for i in range(len(split_ends)):
            if ")" in split_ends[i]:
                split_split_ends = split_ends[i].split(")")
                result = "(".join(split_ends[:i]) + _computation(split_split_ends[0]) + \
                         ")".join(split_split_ends[1:])
                if len(split_ends[i + 1:]) > 0:
                    result += "(" + "(".join(split_ends[i + 1:])
                break
        print(result)
        parenthesis = "(" in result

    exponents = "^" in result
    while exponents:
        print("Working on exponents")
        split_ends = result.split("^")
        pre = ""
        base = split_ends[0]
        power = split_ends[1]
        post = ""
        for i in range(len(split_ends[0]) - 1, -1, -1):
            if split_ends[0][i] in ["+", "*", "/"]:
                pre = split_ends[0][:i + 1]
                base = split_ends[0][i + 1:]
                break
        for i in range(len(split_ends[1])):
            if split_ends[1][i] in ["+", "*", "/"]:
                power = split_ends[1][:i]
                post = split_ends[1][i:]
                if len(split_ends[2:]) > 0:
                    post += "^" + "^".join(split_ends[2:])
                break
        result = pre + str(pow(float(base), float(power))) + post
        exponents = "^" in result

    is_multi_div = "*" in result or "/" in result
    while is_multi_div:
        print("Working on Multi/Division")
        is_multi = True
        split_ends = []
        for i in range(len(result)):
            if result[i] == "*":
                split_ends = result.split("*")
                break
            elif result[i] == "/":
                split_ends = result.split("/")
                is_multi = False
                break

        pre = ""
        base = split_ends[0]
        multiplier = split_ends[1]
        if is_multi and len(split_ends[2:]) > 0:
            post = "*" + "*".join(split_ends[2:])
        elif len(split_ends[2:]) > 0:
            post = "/" + "/".join(split_ends[2:])
        else:
            post = ""
        for i in range(len(split_ends[0]) - 1, -1, -1):
            if split_ends[0][i] in ["+", "*", "/"]:
                pre = split_ends[0][:i + 1]
                base = split_ends[0][i + 1:]
                break
        for i in range(len(split_ends[1])):
            if split_ends[1][i] in ["+", "*", "/"]:
                print(split_ends[1])
                multiplier = split_ends[1][:i]
                post = split_ends[1][i:]
                print(split_ends[2:])
                if len(split_ends[2:]) > 0:
                    if is_multi:
                        post += "*" + "*".join(split_ends[2:])
                    else:
                        post += "/" + "/".join(split_ends[2:])
                break
        print(pre, base, multiplier, post, sep="\t|\t")
        if is_multi:
            result = pre + str((float(base) * float(multiplier))) + post
        else:
            result = pre + str((float(base) / float(multiplier))) + post
        print(result)
        is_multi_div = "*" in result or "/" in result

    adding = "+" in result
    while adding:
        print("Working on Addition")
        split_ends = result.split("+")
        n = 0
        for stuff in split_ends:
            n += float(stuff)
            print(result)
        result = str(n)
        print(result)
        adding = "+" in result
    return result


class MathFormula(object):
    formula: str
    variables: [str]

    def __init__(self, user_input):
        self.formula = user_input
        self._simplify_formula()
        self._identify_variable()

    def _simplify_formula(self):
        """This function will simplify _formula by doing the following 2 things:

        1: Remove blank space(s).
        2: Add multiplication operator (*) where it's implied (e.g. 3x^2 ==> 3*x^2)
        """
        eq = self.formula.replace(' ', '')
        result = []
        for i in range(len(eq)):
            if i != 0 and ((eq[i].isalpha() or eq[i] == "(") and (eq[i-1].isnumeric() or eq[i-1].isalpha())):
                result.append('*')
            result.append(eq[i])
        self.formula = ''.join(result)

        logging.info(f'function: {self.formula}')

    def _identify_variable(self):
        """This function will identify the variable and append to _variables.

        Next: identify the greek letters (written in the forms of %pi% or /pi or such)
        """
        self.variables = []
        for c in self.formula:
            if c.isalpha() and c not in self.variables:
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
            expression = self._substitute_value(**kwargs)
            for i in range(len(expression)-1, -1, -1):
                if expression[i] == "-" and i != 0 and expression[i-1] not in ["^", "*", "/", "+"]:
                    expression = expression[:i] + "+" + expression[i:]
            answer = _computation(expression)
            return float(answer)

