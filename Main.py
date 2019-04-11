from inicializacao import *
from selecao import *
from cruzamento import vamoCruzar
import numpy as np

populacao = int(input('Informe a população inicial: '))
tamCromossomo = int(input('Informe o tamanho do cromossomo: '))
lista_fenotipos = inicializacao1(populacao, tamCromossomo)
print(lista_fenotipos)
pai1 = getRanking(lista_fenotipos)
pai2 = getTorneio(lista_fenotipos, condicao=pai1)
filho = vamoCruzar(pai1, pai2)
lista_fenotipos = list(lista_fenotipos)
lista_fenotipos.append(np.array(filho))
lista_fenotipos = np.array(lista_fenotipos)
print(f'Escolhido: {pai1} | {pai2}')
print(f'Cruzamento resultante: {filho}')
print(lista_fenotipos)