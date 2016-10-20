#!/usr/bin/python

from __future__ import division
from __future__ import print_function

import ast
import operator as op


__author__ = 'Scott Carpenter'
__license__ = 'gpl v3 or greater'
__email__ = 'scottc@movingtofreedom.org'


# supported operators
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg, ast.Invert: op.invert}


# eval_expr / _eval from: http://stackoverflow.com/a/9558001/2374860
def eval_expr(expr):
    return _eval(ast.parse(expr, mode='eval').body)


def _eval(node):
    if isinstance(node, ast.Num):  # <number> e.g. 1 or -1
        return node.n
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        return operators[type(node.op)](
            _eval(node.left), _eval(node.right)
        )
    elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., ~1
        return operators[type(node.op)](_eval(node.operand))
    else:
        raise TypeError(node)