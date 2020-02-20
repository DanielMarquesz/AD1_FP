import random

def numerosAleatorios(entrada):

    listaRandom = []

    for i in range(1, entrada): # Loop para adicao de números aleatórios
        numAleatorio = random.randint(0, 10)
        listaRandom.append(numAleatorio)


    print('Valores: ', end=' ') # loop para Exibir os valores randomicos do vetor
    for d in range(len(listaRandom)):
        print(listaRandom[d], end=' ')

    print()
    numeroAleatorio = random.choice(listaRandom) # Seleciona um número aleatório da lista

    print('K: ',numAleatorio) # Mostra o número aleatório Slecionado

    if numAleatorio in listaRandom: # verifica se e imprime a posição do numero aleatório da lista
        print('Índice: ',listaRandom.index(numAleatorio))
    else:
        print('Valor não encontrado')


# Programa Principal

entrada = 0
entrada = int(input())
numerosAleatorios(entrada)
