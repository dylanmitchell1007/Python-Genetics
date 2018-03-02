def Pairs(self):        
    #vaiables with '!' operator
    v = [] 
    
    s = '' 
    for char in self.expression:

        if(char is '!'):
            s += '!'
            continue

            #lowercase
        if(ord(char) >= 97 and ord(char) <= 122): 
            c = ''
            if(s is '!'):
                c += s
                c += char
                v.append(c)
                s = ''
            else:
                v.append(char)
            continue

            #uppercase
        if(ord(char) >= 65 and ord(char) <= 90):
            
            C = ''
            if(s is '!'):
                C += s
                C += char
                v.append(C)
                s = ''
            else:
                v.append(char)
            continue
            
    variables = list(set(v)) #REMOVES DUPLICATES
    variables.sort(cmp=None, key=lambda x: x, reverse=False) #SORT THE LIST

    p = variables
    pairs = []
    for var in p:
        if(len(var) > 1):
            continue
        pair = (str(var), "")
        pairs.append(pair)
    for var in p:
        if(len(var) <= 1):
            continue
        pair = (str(var), "")
        pairs.append(pair)

    self.pairs = pairs
    return self.pairs