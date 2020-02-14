'''
Utilizando sub-programação, faça um programa que leia da entrada padrão uma única linha
podendo conter zero ou mais números inteiros. Caso exista(m), escreva qual(is) o(s) número(s)
primo(s). Mostre-o(s) um por linha. Caso a linha lida seja uma string vazia, escreva a
mensagem: “Nenhum Número Foi Lido!!!”.

+++++++++++++++++++++++++++++++++
frase = []
frase = [int(i) for i in input().split()] # entrada de valores inteiros

n = 0
primo = False

for f in range(tamanho):
    n = frase[f]
    if n > 0:
        if n == 1:
            print(n)
        else:
            primo = True
            for g in range(2, n):
                if n % g == 0:
                    primo = False
            if primo == True:
                print(n)
'''
def contaPrimo():
    frase = []
    vazio = []
    frase = [int(i) for i in input().split()]
    if vazio == frase: # entrada de valores inteiros
        print('Nenhum Número Foi Lido!!!')
    else:
        tamanho = len(frase)
        primo = False
        print('Relação de Primo (s) : ')
        for f in range(tamanho):
            n = frase[f]
            if n > 1:
                primo = True
                for g in range(2, n):
                    if n % g == 0:
                        primo = False
                if primo == True:
                    print(n)
        print('Fim da Relação.')

contaPrimo()

