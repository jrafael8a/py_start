# ASync. La programación asincrónica permite ejecutar múltiples tareas de manera concurrente 
# sin bloquear el hilo principal, lo que puede mejorar la eficiencia de tu programa, 
# especialmente cuando se trabaja con tareas de I/O (lectura/escritura en archivos, 
# consultas a bases de datos, solicitudes HTTP, etc.).

# async: 
# Se usa para definir una función asincrónica. Esta función no devuelve un valor inmediatamente, 
# sino un "coroutine" (un tipo especial de generador que puede ser pausado y reanudado).

# await: 
# Se usa dentro de una función async para llamar a otra función asincrónica y esperar su resultado. 
# La ejecución de la función async se detiene hasta que la operación await finaliza.

# Event Loop (asyncio)
# Para ejecutar funciones asincrónicas, Python usa un bucle de eventos o event loop. 
# El módulo asyncio proporciona las herramientas necesarias para trabajar con este bucle de eventos, 
# gestionar tareas y ejecutar código asincrónico.

# El event loop maneja las corutinas, programando y ejecutando las tareas cuando los recursos 
# están disponibles (por ejemplo, cuando la operación de I/O ha terminado).

# asyncio.run()
# Esta es la forma moderna de ejecutar un event loop en Python. Toma una corutina (función async) 
# y la ejecuta en el bucle de eventos.

# Ejemplo de uso de async en 2 tareas que toman tiempo
# Sin async, las tareas se ejecutarian primero la tarea 1, espera a que esta termine, y luego
# se ejecutaria la tarea 2, y espera a que esta termine.
# Pero usando programacion asincrona, ambas tareas comienzan al mismo tiempo. Veamos:

# Programacion asincrona (No Bloqueante) [RECOMENDADO]
import asyncio
print("Ejemplo de programacion asincrona (No Bloqueante) [RECOMENDADO]")

async def tarea_1():
    print("Tarea asincrona 1 empezando")
    await asyncio.sleep(3)  # Simula una espera de 1 segundo
    print("Tarea asincrona 1 terminada")

async def tarea_2():
    print("Tarea asincrona 2 empezando")
    await asyncio.sleep(2)  # Simula una espera de 2 segundos
    print("Tarea asincrona 2 terminada")

async def main():
    # Lanza las tareas para que se ejecuten concurrentemente
    await asyncio.gather(tarea_1(), tarea_2())

# Ejecuta el bucle de eventos
asyncio.run(main())


# Programacion sincronica (Bloqueante) [NO RECOMENDADO]
import time
print("Ejemplo de programacion sincronica (Bloqueante) [NO RECOMENDADO]")

def tarea_1():
    print("Tarea sincronica 1 empezando")
    time.sleep(3)  # Simula una espera de 1 segundo de manera bloqueante
    print("Tarea sincronica 1 terminada")

def tarea_2():
    print("Tarea sincronica 2 empezando")
    time.sleep(2)  # Simula una espera de 2 segundos de manera bloqueante
    print("Tarea sincronica 2 terminada")

def main():
    # Lanza las tareas de manera secuencial
    tarea_1()
    tarea_2()

# Ejecuta las tareas de manera secuencial
main()
