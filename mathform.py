"""This module contains a class for interpreting user inputted math formula.

MathFormula first checks if the input can be understood, and evaluates given a value.
"""

from math import *

class MathFormula(object):
    _formula: str
    _variables: [str]
    _order_of_operation: [str]

    def __init__(self, user_input):
        self.formula = self.read_function(user_input)
        self.variables = self.identifyVar()

    @staticmethod
    def read_function(user_input):
        """This function will modify the given

        Args:
            user_input: string -- the function inputted by the user

        Returns:
            a string that contains cleaner function

        """
        eq = "".join([c for c in user_input if c != " "])
        result = ""
        for i in range(len(eq)):
            if i!=0 and (eq[i].isalpha() or eq[i] == "(") and (eq[i-1].isnumeric() or eq[i-1].isalpha()):
                result += "*"
            result += eq[i]
        print(result)
        return result

    def identifyVar(self):
        # currently not supporting greek letters
        exp_flag = False
        var_list = []
        for c in self.formula:
            if exp_flag:
                if c == "^":
                    exp_flag = False
                elif "e" not in var_list:
                    var_list.append('e')
            if c.isalpha():
                if c == 'e':
                    exp_flag = True
                elif c not in var_list:
                    var_list.append(c)
        return var_list

    def substitute(self, var_list, val_list):
        result = self.formula
        for i in range(len(var_list)):
            if var_list[i] != "e":
                result = str(val_list[i]).join(result.split(var_list[i]))
            else:
                result = ""
                for split_end in result.split('e^'):
                    result += str(val_list[i]).join(split_end.split(var_list[i]))
        if DEBUGGING: print(result)
        return result

    def evaluate(self, val_list):
        def computation(expression):
            result = expression
            parenthesis = "(" in result
            while parenthesis:
                print("Working on Parenthesis")
                splitends = result.split("(")
                for i in range(len(splitends)):
                    if ")" in splitends[i]:
                        splitsplitends = splitends[i].split(")")
                        result = "(".join(splitends[:i]) + computation(splitsplitends[0]) +\
                                 ")".join(splitsplitends[1:])
                        if len(splitends[i+1:]) > 0:
                            result += "(" + "(".join(splitends[i+1:])
                        break
                print(result)
                parenthesis = "(" in result

            exponents = "^" in result
            while exponents:
                print("Working on exponents")
                splitends = result.split("^")
                pre = ""
                base = splitends[0]
                power = splitends[1]
                post = ""
                for i in range(len(splitends[0])-1, -1, -1):
                    if splitends[0][i] in ["+", "*", "/"]:
                        pre = splitends[0][:i+1]
                        base = splitends[0][i+1:]
                        break
                for i in range(len(splitends[1])):
                    if splitends[1][i] in ["+", "*", "/"]:
                        power = splitends[1][:i]
                        post = splitends[1][i:]
                        if len(splitends[2:]) > 0:
                            post += "^" + "^".join(splitends[2:])
                        break
                result = pre + str(math.pow(float(base), float(power))) + post
                if DEBUGGING: print(result)
                exponents = "^" in result

            multidiv = "*" in result or "/" in result
            while multidiv:
                print("Working on Multi/Division")
                isMulti = True
                for i in range(len(result)):
                    if result[i] == "*":
                        splitends = result.split("*")
                        break
                    elif result[i] == "/":
                        splitends = result.split("/")
                        isMulti = False
                        break
                pre = ""
                base = splitends[0]
                multiplier = splitends[1]
                if isMulti and len(splitends[2:])>0:
                    post = "*" + "*".join(splitends[2:])
                elif len(splitends[2:])>0:
                    post = "/" + "/".join(splitends[2:])
                else:
                    post = ""
                for i in range(len(splitends[0])-1, -1, -1):
                    if splitends[0][i] in ["+", "*", "/"]:
                        pre = splitends[0][:i + 1]
                        base = splitends[0][i + 1:]
                        break
                for i in range(len(splitends[1])):
                    if splitends[1][i] in ["+", "*", "/"]:
                        print(splitends[1])
                        multiplier = splitends[1][:i]
                        post = splitends[1][i:]
                        print(splitends[2:])
                        if len(splitends[2:]) > 0:
                            if isMulti:
                                post += "*" + "*".join(splitends[2:])
                            else:
                                post += "/" + "/".join(splitends[2:])
                        break
                print(pre, base, multiplier, post, sep="\t|\t")
                if isMulti:
                    result = pre + str((float(base) * float(multiplier))) + post
                else:
                    result = pre + str((float(base) / float(multiplier))) + post
                print(result)
                multidiv = "*" in result or "/" in result

            adding = "+" in result
            while adding:
                print("Working on Addition")
                splitends = result.split("+")
                n = 0
                for stuff in splitends:
                    n += float(stuff)
                    print(result)
                result = str(n)
                print(result)
                adding = "+" in result
            return result
        if type(val_list) is not list:
            val_list = [val_list]
        if len(val_list) != len(self.variables):
            print("ERROR: values-to-variables mismatch")
        else:
            var_list = sorted(self.variables)
            expression = self.substitute(var_list, val_list)

            for i in range(len(expression)-1, -1, -1):
                if expression[i] == "-" and i != 0 and expression[i-1] not in ["^", "*", "/", "+"]:
                    expression = expression[:i] + "+" + expression[i:]
            answer = computation(expression)
            return float(answer)
