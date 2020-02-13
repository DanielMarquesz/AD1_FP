

lista = ['gol','47P','a','futebol','laranja','8 x9','13 XL','ou','Juca 2','ué','Aaaaá']
tamanho = []

for i in range(len(lista)): # Número de Dígitos
    string = lista[i]
    total = 0
    for ch in lista[i]: # transformar essa parte em uma função
        if ch.isdigit():
            total += 1
            stringAt = lista[i]
            print(total)
            tamanho.append(total)

print(tamanho)
string = 'm4rm3m4md4'
soma = 0

def digitos():
    soma = 0
    for i in string:
        if i in "0123456789":
            soma += 1
return soma
