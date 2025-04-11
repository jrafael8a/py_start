"""
numeros = range(1,200)

def es_primo(numero):
    for iteracion in range(2,numero):
        if (numero%iteracion) == 0:
            return False
    return True

primos =  list(filter(es_primo, numeros))

print(primos)

"""

print("\nObteniendo numeros primos sin filter")

numeros = range(1,200)
for x in numeros:
    es_primo = True
    for y in range(2,x):
        if (x%y)==0:
            es_primo=False
            break
    if es_primo: 
        print(x,end=", ")