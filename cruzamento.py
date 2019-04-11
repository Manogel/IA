import random as rd

selecionado1 = [1, 0, 0, 1, 0, 0, 1, 1]
selecionado2 = [0, 1, 1, 0, 1, 0, 0, 1]


def getFenotipo(lista):
    str1 = ''.join(str(e) for e in lista)
    str1 = '0b' + str1
    return int(str1, 2)


def uniponto(escolhido1, escolhido2):
    sorteio1 = rd.choice(range(len(escolhido1)))
    print(f'Ate o index {sorteio}')
    filho = escolhido1[:sorteio+1] + escolhido2[sorteio+1:]
    return filho


def multiponto(escolhido1, escolhido2):
    sorteio1 = rd.choice(range(len(escolhido1)))
    sorteio2 = rd.choice(range(len(escolhido1[sorteio1:])))
    sorteio2 += sorteio1
    print(f'de index {sorteio1} ate {sorteio2}')
    filho = escolhido1[:sorteio1] + \
        escolhido2[sorteio1: sorteio2+1] + escolhido1[sorteio2+1:]
    return filho


def aritmetico(escolhido1, escolhido2):
    filho = str(bin(getFenotipo(escolhido1) + getFenotipo(escolhido2)))
    filho = list(filho.split('0b')[1])
    return [int(value) for value in filho]


def mutacaoFlip(filho):
    print(filho)
    for index in range(len(filho)):
        filho[index] = rd.choice([0, 1])
    return filho


def mutacaoTroca(filho):
    print(filho)
    while True:
        sorteio1 = rd.choice(range(len(filho)))
        sorteio2 = rd.choice(range(len(filho)))
        if sorteio1 != sorteio2:
            break
    print(f'Sorteada as posições {sorteio1} {sorteio2}')
    if filho[sorteio1] == 1:
        filho[sorteio1] = 0
    else:
        filho[sorteio1] = 1
    if filho[sorteio2] == 1:
        filho[sorteio2] = 0
    else:
        filho[sorteio2] = 1
    return filho


print(mutacaoFlip(selecionado1))
