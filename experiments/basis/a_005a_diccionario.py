# Los diccionarios son como listas, pero con 2 pares de datos.

persona = {"nombre": "Juan", "apellido": "Perez", "edad": 25}
print(persona["nombre"])
print(persona["edad"])

# Para Modificar un valor simplemente se hace una nueva asignacion llamando por el nombre de la clave
persona["edad"] = 26
print(persona["edad"])
# Al final son como listas, pero en lugar de indices, tienen nombres

# Usando el método update(): 
# Si deseas agregar varios pares clave-valor, puedes usar el método update(), 
# que también sobrescribe los valores si la clave ya existe.

persona.update({"edad": 28, "direccion": "Madrid"})
print(persona)


print("Tambien se pueden agregar con el simbolo | ")
persona = persona | {"Telefono": "8765-4321"}
print(persona)

print(); print()
print("Forma alternativa de crear un Diccionario: \n Usando diccionario por comprensión")
# La sintaxis {clave: valor for elemento in iterable} permite construir un diccionario de manera más compacta.
cuadrados = {1, 2, 3, 4, 7}
print({num: num**2 for num in cuadrados})


