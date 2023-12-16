__all__ = ["module"]    # Escribimos __all__ para permitir la notación de *
# module es el nombre del archivo SIN .py
# ahora podemos escribir from module_test import *
# => module.f() ahora funciona porque lo definimos aquí en el archivo init con __all__


# Referencia 1))
from . import module
# Desde el modulo actual, importa el archivo "nombre de archivo"
