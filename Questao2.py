'''
Utilizando sub-programação, faça um programa que leia da entrada padrão uma única linha
podendo conter zero ou mais números inteiros. Caso exista(m), escreva qual(is) o(s) número(s)
primo(s). Mostre-o(s) um por linha. Caso a linha lida seja uma string vazia, escreva a
mensagem: “Nenhum Número Foi Lido!!!”.

'''

frase = []
frase = [int(i) for i in input().split()] # entrada de valores inteiros

for f in range(len(frase)):
    if frase[f] % frase[f] == 0 and frase[f] % 1 == frase[f]:
        print(frase[f])
