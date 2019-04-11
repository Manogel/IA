import math
import random as rd
from inicializacao import getFenotipo

def getFitness(list_fenotipo):
    fit = list()
    for value in list(list_fenotipo):
        fitness = pow(getFenotipo(list(value)), 2)
        fit.append(fitness)
    fit.sort()
    return fit

def getRanking(list_fenotipo, condicao = None):
    escolha = []
    while True:
        maior = -1
        for value in list(list_fenotipo):
            aux = getFenotipo(list(value))
            if aux > maior:
                maior = aux
                escolha = list(value)
        if escolha != condicao and escolha != []:
            return escolha

def getTorneio(list_fenotipo, divisao=2, condicao = None):
    quantidade = math.ceil(len(list_fenotipo)/divisao)
    time = list()
    for x in range(divisao):
        conjunto = list_fenotipo[(quantidade*x):(quantidade*(x+1))]
        time.append(conjunto)
    
    selecionado = []
    while True:
        x = 0
        for selecao in time:
            escolha = rd.choice(selecao)
            fenotipo = getFenotipo(list(escolha))
            #print(escolha)
            if fenotipo > x:
                x = fenotipo
                selecionado = escolha
        if list(selecionado) != condicao and x != 0:
            return list(selecionado)
         
def getRoleta(list_fenotipo, condicao = None):
    tamCromossomo = len(list_fenotipo[0])
    lista_fitness = getFitness(list_fenotipo)
    #print(lista_fitness)
    total = 0
    for fit in lista_fitness:
        total += fit
    while True:
        escolha = rd.randrange(total+1)
        #print(escolha)
        fenotipo_escolhido = []
        for fit in lista_fitness:
            if fit == escolha:
                fenotipo_escolhido = getGenes(fit, tamCromossomo)
                break
            elif fit > escolha:
                fenotipo_escolhido = getGenes(fit, tamCromossomo)
                break
            elif escolha >= lista_fitness[-1]:
                fenotipo_escolhido = getGenes(lista_fitness[-1], tamCromossomo)
                break
        if fenotipo_escolhido != condicao and fenotipo_escolhido != []:
            return fenotipo_escolhido

def getGenes(fit, tamCromossomo):
    fenotipo = int(math.sqrt(fit))
    #print(fenotipo)
    fenotipo = str(bin(fenotipo).split('0b')[1])
    #print(fenotipo)
    while len(fenotipo) < tamCromossomo:
        fenotipo = '0'+ fenotipo
    return [int(value) for value in list(fenotipo)]





