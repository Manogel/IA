import math
import random as rd
def getFitness(list_fenotipo):
    fit = list()
    for value in list_fenotipo:
        x = pow(value, 2)
        fit.append(x)
    return fit

def getRanking(list_fenotipo, divisao):
    quantidade = math.ceil(len(list_fenotipo)/divisao)
    time = list()
    for x in range(divisao):
        conjunto = list_fenotipo[(quantidade*x):(quantidade*(x+1))]
        if conjunto != None: time.append(conjunto)
    
    #print(time)
    x = 0
    for selecao in time:
        escolha = rd.choice(selecao)
        #print(escolha)
        if escolha > x:
            x = escolha
    return x
         
def getTorneio(list_fenotipo):

    lista_fitness = getFitness(list_fenotipo)
    total = 0
    for fit in lista_fitness:
        total += fit

    print(lista_fitness)
    escolha = rd.randrange(total+1)
    print(escolha)
    for index, fit in enumerate(lista_fitness):
        if fit == escolha:
            return lista_fenotipo[index]
        elif fit > escolha:
            return list_fenotipo[index-1]
    return list_fenotipo[-1]





