import random as rd
import numpy as np 
import math

def getFenotipo(lista):
    str1 = ''.join(str(e) for e in lista)
    str1 = '0b'+ str1
    return int(str1, 2)

def getCromossomo1():
    cromossomo = [0 , 1]
    return rd.choice(cromossomo)

def getCromossomo2():
    cromossomo = range(1, 11)
    x = rd.choice(cromossomo)
    if x <= 3:
        # 30%
        return 1
    else:
        # 70%
        return 0

def inicializacao1(popInicial, tamCromossomo):
    lista_fenotipo = list()
    matriz = []
    for x in range(popInicial):
        aux = []
        for coluna in range(tamCromossomo):
            """ if x == math.ceil(popInicial/2):
                aux = [1]*tamCromossomo
                break """
            aux.append(getCromossomo2())
        f = getFenotipo(aux)
        print(f'Fenotipo gerado: {f}')
        lista_fenotipo.append(f)
        matriz.append(np.array(aux))
    print(np.array(matriz))
    return lista_fenotipo

def inicializacao2(popInicial, tamCromossomo):
    lista_fenotipo = list()
    matriz = list()
    for x in range(popInicial):
        while True:
            aux = []
            for coluna in range(tamCromossomo):
                aux.append(getCromossomo2())
            fenotipo = getFenotipo(aux)
            if fenotipo not in lista_fenotipo:
                lista_fenotipo.append(fenotipo)
                break
        matriz.append(np.array(aux))
    print(np.array(matriz))




