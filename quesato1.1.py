'''
Faça um programa que leia strings da entrada padrão, até que a string vazia (“”) seja digitada.
Caso a primeira string lida seja vazia, escreva a mensagem “Nenhuma String Não Vazia Foi Lida!!!”. Caso contrário escreva:

(1) Qual a string que tem maior comprimento; caso haja empate escreva a primeira delas;
(2) Qual a string possui mais dígitos, isto é, contém caracter(es) na string “0123456789”.
Caso haja empate escreva a última delas. Caso nenhuma possua dígitos escreva: “Nenhuma String Contém Dígito!!!”
(3) Qual a quantidade de strings formadas apenas de vogais minúsculas e sem acento, isto é, contidas na string “aeiou”.
'''

def maiorPalavra(entrada):
    palavraAtual = entrada
    if len(palavraAtual) < len(entrada): # Verifica a maior string digitada
            stringAtual = entrada
            print('Primeira de Maior Comprimento: ',stringAtual)


stringAtual = 0
palavra = input() #lê a primeira palavra

if palavra == "":                       # Verifica se os valores são diferentes de Vazio
    print("Nenhuma String Não Vazia Foi Lida!!!")
else:
    while palavra != "":
        palavraAtual = palavra
        if len(palavraAtual) > len(palavra): # Verifica a maior string digitada
            stringAtual = palavra
        print('Primeira de Maior Comprimento: ',stringAtual)

        palavra = input()
