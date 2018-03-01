import os

class CNF(object):
    def __init__(self, expression):
        self.expression = expression
        self.py_expression = self.GetPyExpression()
        self.pairs = []
        self.variables = []
        self.clauses = []
        self.GetVariables()
    def GetPyExpression(self):
        return self.expression.replace('*', 'and').replace('+', 'or').replace('!', 'not')
    def GetVariables(self):
        rawVariables = []
        for char in self.expression:
            if(ord(char) >= 97 and ord(char) <= 122):
                rawVariables.append(char)
                continue
            if(ord(char) >= 65 and ord(char) <= 90):
                rawVariables.append(char)
                continue

        self.variables = list(set(rawVariables))
        self.variables.sort(cmp=None, key=lambda x: x, reverse=False)
        return self.variables

    def PrintInfo(self):
        print 'expression ' + self.expression
        print 'py_expression ' + self.py_expression
        print 'variables ' + str(self.variables)
        print 'clauses ' + str(self.clauses)
        print 'pairs ' + str(self.pairs)

def main():
    cnfparser = CNF('(a) * (b) * (c) * (d)')
    cnfparser.PrintInfo()

main()
