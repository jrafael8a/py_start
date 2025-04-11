def get_largest_number(numbers, n):
    # A continuacion inicia un docstring
    # El docstring es una cadena de caracteres que describe la función
    # Debe estar entre comillas triples dobles
    # El docstring debe estar en la primera línea de la función
    # Python ignora el docstring, pero puede ser accedido por la funcion help()
    # Por lo que se usa principalmente para documentacion.
    """
    This function returns the largest number from a list of numbers.
    :parametro numbers: List of numbers
    :parametro n: Number of elements to consider
    :return: Largest number
    """
    numbers.sort()
    return numbers[-n]

nums =[2,3,4,1,34,123,321,1]

print(nums)
largest_num = get_largest_number(nums, 2)
print(nums)
print(largest_num)
# Salida:
# [2, 3, 4, 1, 34, 123, 321, 1]
# [1, 1, 2, 3, 4, 34, 123, 321]
# 123

# En este ejemplo, la función get_largest_number recibe una lista de números y un número n.
# La función ordena la lista de números y devuelve el n-ésimo número más grande de la lista.
# En este caso, la función devuelve el segundo número más grande de la lista.
# La función no modifica la lista original, ya que la lista se pasa por referencia.
# Sin embargo, la función sort() modifica la lista original.
# Para evitar esto, se puede hacer una copia de la lista original antes de ordenarla.

# Para hacer una copia de la lista, se puede usar el método copy() o la función list().
print("")
print("")
print("Modificando el codigo para que el metodo sort() no modifique la lista original")
def get_largest_number(numbers, n):
    numbers = numbers.copy()  # Se crea una copia de la lista original
    numbers.sort()  # Se ordena la copia
    return numbers[-n]  # Se obtiene el n-ésimo número más grande

# Comentario sobre numbers = numbers.copy()
# en Python, las variables dentro de una función son locales por defecto. 
# Esto significa que la variable numbers dentro de la función es independiente 
# de la variable numbers fuera de la función, incluso si tienen el mismo nombre.

nums =[2,3,4,1,34,123,321,1]

print(nums)
largest_num = get_largest_number(nums, 2)
print(nums)
print(largest_num)

# Salida:
# [2, 3, 4, 1, 34, 123, 321, 1]
# [2, 3, 4, 1, 34, 123, 321, 1]
# 123
# En este ejemplo, la función get_largest_number recibe una lista de números y un número n.
# La función hace una copia de la lista de números y luego ordena la copia.
# La función devuelve el n-ésimo número más grande de la lista.
# La lista original no se modifica, ya que se hizo una copia de la lista original.
