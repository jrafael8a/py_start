print("\n\nEjemplo 4: Uusando filter para obtener Numeros Primos")
# Con filter() podemos crear una funcion que detecte si un numero es primo
# y si lo es, que lo imprima, sino no.

nums=range(1,100)

def es_primo(num):
    for x in range (2,num):
        if (num%x) == 0:
            return False
        return True
    

# print(list(nums))
primos = list(filter(es_primo, nums))

print(primos)