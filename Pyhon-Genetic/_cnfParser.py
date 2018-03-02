import os

class CNF(object):
    def __init__(self, data):
        self.expression = data
        self.original_expression = self.expression
        self.py_expression = self.PythonExpression()
        self.pairs = []
        self.variables = []
        self.Pairs()
        self.Variables()
    
    def PythonExpression(self):
        return self.expression.replace('*', 'and').replace('+', 'or').replace('!', 'not ')

    def Variables(self):
        variables = []
        
        for c in self.expression:
            #lowercase
            if(ord(c) >= 97 and ord(c) <= 122):
                variables.append(c)
                continue
            #uppercase
            if(ord(c) >= 65 and ord(c) <= 90):
                variables.append(c)
                continue


        self.variables = list(set(variables))
        self.variables.sort(cmp=None, key=lambda x: x, reverse=False)
        return self.variables
    
    def Pairs(self):
        variables = []
        
        s = '' 
        for c in self.expression:
            if(c is '!'):
                s += '!'
                continue

            #lowercase
            if(ord(c) >= 97 and ord(c) <= 122):
                C = ''
                if(s is '!'):
                    C += s
                    C += c
                    variables.append(C)
                    s = ''
                else:
                    variables.append(c)
                continue

            #uppercase
            if(ord(c) >= 65 and ord(c) <= 90):
                C = ''
                if(s is '!'):
                    C += s
                    C += c
                    variables.append(C)
                    s = ''
                else:
                    variables.append(c)
                continue

        pairs = []
        for val in variables:
            pair = (val, '')
            pairs.append(pair)

        self.pairs = pairs
        return self.pairs

    def _get_pairs(self):
        return self.pairs

    def PrintInfo(self):
        print 'Expression(' + self.expression + ')'
        print 'Python Expression(' + self.py_expression + ')'
        print 'Pairs(' + str(self.pairs) + ')'
        print 'Variables(' + str(self.variables) + ')'
        
    def Inject(self, values):
        for i in range(0, len(self.pairs), 1):
            value = values[i]
            p = self.pairs[i]
            newpair = (p[0], value)
            self.pairs[i] = newpair

        e = ''
        for c in self.expression:
            #lowercase
            if(ord(c) >= 97 and ord(c) <= 122):
                for pair in self.pairs:                    
                    v = pair[0]
                    var = ''
                    if(len(v) > 1):
                        var = v[1]
                    else:
                        var = v

                    value = pair[1]
                    if(c is var):
                        e += value
                continue
            
            #uppercase
            if(ord(c) >= 65 and ord(c) <= 90):
                for pair in self.pairs:
                    var = pair[0]
                    value = pair[1]
                    if(c is var):
                        e += value
                continue
                        
            else:
                e += c
                continue
        
        self.expression = e
        self.py_expression = self.PythonExpression()
        
    def TestExpression(self):
        return 'Result(' + str(bool(eval(self.py_expression))) + ')'

    def _test_expression(self):
        return bool(eval(self.py_expression))

def main():
    e = CNF('(a) * (b) * (c) * (!d)')
    #e.LoadRandomExpression()
    e.Inject('1110')
    e.PrintInfo()
    print e.TestExpression()

main()