import os
import random
from _chromosome import *
def Selection(population):
    p1 = [100]
def Mutation(mutationRate, gene):
    if mutationRate > 100:
        mutationRate = 100
    if mutationRate < 0:
        mutationRate = 0
    mutatedC = ""
    for i in range(0, len(gene._getDNA())):
        x = random.uniform(0, 100)
        if x <= mutationRate:
            m = bool(int(gene.DNA[i]))
            mutatedC += str(int(not m))

        else:
            mutatedC += gene.DNA[i]
    return mutatedC
def Crossover(pivot, p1, p2):
    child1DNA = ""
    child2DNA = ""

    for i in range(0, pivot):
        child1DNA += p1.DNA[i]
        child2DNA += p2.DNA[i]

    for x in range(pivot, len(p1.DNA)):
        child1DNA += p2.DNA[x]
        child2DNA += p1.DNA[x]


    child1 = Chromosome(child1DNA)
    child2 = Chromosome(child2DNA)

    return[child1, child2]








def main():
#     c = Chromosome("0000")
#     print c._getDNA()
    p1 = Chromosome("1111")
    p2 = Chromosome("0000")
    print p1._getDNA()
    print p2._getDNA()

    children = Crossover(2, p1, p2)

    for child in children:
        print child._getDNA()   
#     c.DNA = Mutation(100, c)
#    print c._getDNA()

main()
