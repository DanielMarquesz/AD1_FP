import random


def gerarMatriz(linhas, colunas, C, D):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(random.randint(C, D))
        matriz.append(linha)
    return matriz

def mostraMatriz(matriz):
    for lin in range(len(matriz)):
        for col in range(len(matriz[lin])):
            print(matriz[lin][col], end=' ')
        print()
    print()

def calculaMedia(values, A, B):
    total = 0
    for j in range(A):
        total = total + sum(values[j])
    dimensaoMatriz = A * B
    total = total / dimensaoMatriz
    print('Média dos valores Sorteados:\n{:.1f}'.format(total))




A, B, C, D = [int(i) for i in input().split()] # Entrada dos Valores


values = gerarMatriz(A, B, C, D) # Atribui a matriz inteira a variável values
print('Counteúdo da Matriz:')
mostraMatriz(values) # Exibe a Matriz
calculaMedia(values, A, B) # Calcula e Exibe a média dos valores da matriz








