"""
Evaluate Reverse Polish Notation
Solved
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
Return the integer that represents the evaluation of the expression.
    The operands may be integers or the results of other operations.
    The operators include '+', '-', '*', and '/'.
    Assume that division between integers always truncates toward zero.

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
"""

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # ["1","2","+","3","*","4","-"]
        
        stck = []
        operators = {
            "+": (lambda a, b: a + b),
            "-": (lambda a, b: a - b),
            "/": (lambda a, b: int(a / b)),
            "*": (lambda a, b: a * b),
        }

        for t in tokens:
            print(stck)
            if t in operators:
                b = stck.pop()
                a = stck.pop()
                stck.append(operators[t](a,b))
            else:
                stck.append(int(t))

        return stck[0] 
