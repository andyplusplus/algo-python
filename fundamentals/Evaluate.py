__author__ = 'andy'

from collections import deque

def evalute(expr):
    operators = deque()
    oprands = deque()
    exprlist = _getExprList(expr)
    for str in exprlist:
        if str == ")" and len(operators)>0:
            val2 = oprands.pop();val1 = oprands.pop()
            op = operators.pop()
            result = eval("%s%s%s" % (val1, op, val2))
            oprands.append(result)
        elif str.isnumeric():
            oprands.append(str)
        else:
            operators.append(str)
    assert(len(operators)==0)
    assert(len(oprands)==1)
    return oprands.pop()

#(1+((2+3)*(4*15)))
#remove "("
#add digit and oper to list
def _getExprList(expr):
    expr.replace("(", "")
    for c in "+-*/)":
        expr = expr.replace(c, " %s " % c)
    expr = expr.replace("(", "")
    list = expr.split()
    return list

from unittest import TestCase
class Test_(TestCase):
    def test(self):
        result = evalute("(1+((2+3)*(4*15)))")
        print(result)
        self.assertTrue(301 == int(result))
