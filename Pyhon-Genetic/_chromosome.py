import random

class Chromosome(object):
    def __init__(self, genes):
        self.DNA = genes 
    
    def Generate(self, count):
        self.DNA = ""
        for i in range(0, count, 1):
            x = random.randint(0, 1)
            self.DNA += str(x)

    def _getDNA(self):
        return self.DNA

def main():
    c = Chromosome('')
    c.Generate(4)
    print c._getDNA()

main()