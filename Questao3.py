import random


def gerarMatriz(linhas, colunas, C, D): # Cria a Matriz
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(random.randint(C, D))
        matriz.append(linha)
    return matriz

def mostraMatriz(matriz): # Mostra a matriz na tela
    for lin in range(len(matriz)):
        for col in range(len(matriz[lin])):
            print(matriz[lin][col], end=' ')
        print()
    print()

def calculaMedia(values, A, B): # Calcula a media dos valores
    total = 0
    for j in range(A):
        total = total + sum(values[j])
    dimensaoMatriz = A * B
    total = total / dimensaoMatriz
    print('Média dos valores Sorteados:\n{:.1f}'.format(total))
    return total

def bordaSuperior(matriz, B): # Borda Superior
    bordaSup = []
    for i in range(B):
        bordaSup.append(matriz[0][i])
    return bordaSup

def bordaEsquerda(matriz, A): # Borda Esquerda
    bordaEsq = []
    for i in range(A):
        bordaEsq.append(matriz[i][0])
    return bordaEsq

def bordaDireita(matriz, A, B): # Borda Direita
    bordaDir = []
    for i in range(A):
        bordaDir.append(matriz[i][B - 1])
    return bordaDir

def bordaInferior(matriz,A ,B): #Borda Inferior
    bordaInf = []
    for i in range(B):
        bordaInf.append(matriz[A -1][i])
    return bordaInf

A, B, C, D = [int(i) for i in input().split()] # Entrada dos Valores

valoresBorda = []
values = gerarMatriz(A, B, C, D) # Atribui a matriz inteira a variável values
print('Counteúdo da Matriz:')
mostraMatriz(values) # Exibe a Matriz
media = calculaMedia(values, A, B) # Calcula e Exibe a média dos valores da matriz
print()
# Atrubuição dos valores das bordas
superior = bordaSuperior(values, B)
esquerda = bordaEsquerda(values, A)
direita = bordaDireita(values, A, B)
inferior = bordaInferior(values,A ,B)

bordasTotal = superior + esquerda + direita + inferior

print('Relação de Valores nas Bordas Acima da Média:')
for i in range(len(bordasTotal)):
    if bordasTotal[i] > media:
        print(bordasTotal[i])
