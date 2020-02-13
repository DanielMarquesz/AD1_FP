'''
Faça um programa que leia strings da entrada padrão, até que a string vazia (“”) seja digitada.
Caso a primeira string lida seja vazia, escreva a mensagem “Nenhuma String Não Vazia Foi Lida!!!”. Caso contrário escreva:

(1) Qual a string que tem maior comprimento; caso haja empate escreva a primeira delas;
(2) Qual a string possui mais dígitos, isto é, contém caracter(es) na string “0123456789”.
Caso haja empate escreva a última delas. Caso nenhuma possua dígitos escreva: “Nenhuma String Contém Dígito!!!”
(3) Qual a quantidade de strings formadas apenas de vogais minúsculas e sem acento, isto é, contidas na string “aeiou”.

'''
def contarVogaisDigitos(pals):
    qVogs, qDigs = 0, 0
    for p in pals:
        for letra in p:
            if letra in "0123456789":
                qDigs += 1
            elif letra.upper() in "AEIOU":
                qVogs += 1
    return qVogs, qDigs



vetor = []
entrada = input()
cont = 0


vetor.append(entrada)
stringAtual = entrada
maiorVogal, maiorDigito = contarVogaisDigitos(entrada)

if entrada == "":                       # Verifica se os valores são diferentes de Vazio
    print("Nenhuma String Contém Dígito!!!")
else:
    while entrada != "":                # Recebe os valores na lista
        entrada = input()
        vetor.append(entrada)
    for c in range(len(vetor)):
        if len(stringAtual) < len(vetor[c]): # Maior Digitado
            stringAtual = vetor[c]
            print('Primeira de Maior Comprimento: ',stringAtual)


for i in range(len(vetor)):
    palavra = vetor[i]
    vogais, digitos =  contarVogaisDigitos(palavra) # retorna o número de vogais e digitos(numeoros de cada item)
    #print("a palavra",vetor[i],'tem',vogais,'vogais e',digitos,'digitos')
    if maiorDigito < digitos:
        maiorDigito = vetor[i]
        print('A string que possui a maior quantidade de dígitos é: ',maiorDigito)

    if maiorVogal < vogais:
        maiorVogal = vetor[i]
        print('A string que possui a maior quantidade de vogais é: ',maiorVogal)

