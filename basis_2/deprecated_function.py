# La funcion deprecated es muy util en python cuando creamos una nueva funcion y queremos
# dejar de usar la anterior. A continuacion te mostrare un ejemplo en el cual
# el mismo IDE nos dara una advertencia cuando usemos una funcion "deprecated"
# y podremos indicarle cual es la nueva funcion que debe usar

from warnings import deprecated

@deprecated("Use 'nueva_funcion() instead!")
def vieja_funcion() -> None:
    print("vieja_funcion() ha sido llamada!")


def nueva_funcion() -> None:
    print("nueva_funcion() ha sido llamada!")



vieja_funcion()


# Con solo una linea de codigo:
#   @deprecated("Use 'nueva_funcion() instead!")
# (Bueno, 2 lineas, si contamos el import)
# Conseguimos alertar al IDE, al equipo de programacion y a nosotros mismos
# sobre ya no usar la funcion obsoleta y a la vez indicar cual es la nueva funcion