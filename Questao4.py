'''
A, B = map(int, input().split())

while B != 0:
    resto = A % B
    A = B
    B = resto
print(A)

'''

# Funções / Procedimentos
def mdc(A, B):
    while A != '-1' or B != '-1':
        while B != 0:
            resto = A % B
            A = B
            B = resto
        print(A)
        A, B = map(int, input().split())
        if A < 1 and B < 1:
            break
    mdc(A, B) # Chamada Recursiva da função/ Procedimento

# Programa principal
A, B = map(int, input().split())
mdc(A, B)




