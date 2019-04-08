from inicializacao import *
from selecao import *

populacao = int(input('Informe a população inicial: '))
tamCromossomo = int(input('Informe o tamanho do cromossomo: '))
lista_fenotipos = inicializacao1(populacao, tamCromossomo)
print(f'Escolhido: {getTorneio(lista_fenotipos)}')