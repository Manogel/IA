import random as rd

selecionado1 = [0,0,0,0]
selecionado2 = [1,1,1,1]




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
    filho = escolhido1[:sorteio1+1] + escolhido2[sorteio1+1: sorteio2+1] + escolhido1[sorteio2+1 :]
    return filho

print(multiponto(selecionado1, selecionado2))
