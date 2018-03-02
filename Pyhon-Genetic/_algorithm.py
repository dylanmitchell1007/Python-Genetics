import os
from _genetic import *
from _chromosome import Chromosome
from _cnfParser import CNF

class GeneticAlgorithm(object):
    def __init__(self):
        self.generation = 1
        self.population = []
        self.scoredpopulation = []
        self.done = False
        self.file = open('GeneticAlgorithmLog.txt', 'w+')

    def CreatePopulation(self, length, count):
        population = []
        for x in range(0, count, 1):
            c = Chromosome("")
            c.Generate(length)
            population.append(c)
        return population

    def Fitness(self, expression):
        for c in self.population:
            expression.expression = expression.original_expression
            expression.Inject(c._getDNA())
            
            pairs = expression._get_pairs()

            score = 0
            finalscore = 0
            length = len(c._getDNA())
            for pair in pairs:
                value = pair[1]
                variable = pair[0]
                
                if('!' in variable):
                    if(value is '0'):
                        score += 1
                else:
                    if(value is '1'):
                        score += 1
            
            finalscore = (float(score) / length) * 100

            scoredchromosome = (c, finalscore)
            self.scoredpopulation.append(scoredchromosome)

        self.scoredpopulation.sort(cmp=None, key=lambda x: x[1], reverse=True)
        self.population = []
        for c in self.scoredpopulation:
            self.population.append(c[0])
            
    def CheckSolution(self, expression):
        s = self.population[0]

        expression.expression = expression.original_expression
        expression.Inject(s._getDNA())

        return expression._test_expression()

    def Print(self, expression):
        os.system('cls')
        expression.expression = expression.original_expression
        print('Expression(' + str(expression.expression) + '\n')
        p = self.scoredpopulation[0]
        dump = ('Best Chromosome(' + str(p[0]._getDNA()) + ')', str(p[1]), 'Generation: ' + str(self.generation))
        print(str(dump) + '\n')

    def WritetoFile(self, expression):
        expression.expression = expression.original_expression
        self.file.write('Expression(' + str(expression.expression) + ')' + '\n')

        for p in self.scoredpopulation:
            dump = ('Chromosome(' + str(p[0]._getDNA()) + ')', str(p[1]), 'Generation: ' + str(self.generation))
            self.file.write(str(dump) + '\n')

    def Run(self, expression):
        count = len(expression.Variables())
        self.population = self.CreatePopulation(count, 10)
        while not self.done:
            if(self.generation >= 500):
                print self.generation
                self.Print(expression)
                self.WritetoFile(expression)
                os.system('pause')
                return

            self.Fitness(expression)
            self.done = self.CheckSolution(expression)
            self.Print(expression)
            self.WritetoFile(expression)
            
            if(self.done):
                print 'Solution(' + self.population[0]._getDNA() + ')'
                self.Print(expression)
                self.WritetoFile(expression)
                return

            pivot = int(count / 2)
            mutationrate = 25

            g = Selection(self.population)
            self.population = []
            self.population = Crossover(pivot, g[0], g[1])
            self.generation += 1
            for c in self.population:
                c.DNA = Mutation(mutationrate, c)
        self.file.close()

def main():
    a = GeneticAlgorithm()
    e = CNF('(!a) * (b) * (c) * (!d) * (!e) * (!f)')
    a.Run(e)
    a.file.close()
    print 'Finished'
    

main()