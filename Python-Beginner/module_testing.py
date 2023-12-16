# Importamos el módulo desde la carpeta module_test

import csv
import sys
import module_test
from module_test import module
# Se carga module_test con solo una parte, que es el archivo module
module.f()

# Ahora quiero cargar toda la carpeta
# No funciona así directamente, hay que hacer un cambio en el archivo __init__.py
# Referencia 1))

module_test.module.f()
# Sintaxis: nombre_de_la_carpeta_del_modulo.nombre_del_archivo.nombre_de_la_funcion()

print(sys.version)

# CSV: valores separados por comas
with open("archivo.csv", newline='') as file:
    csv_file = csv.reader(file, delimiter=";")
    # delimiter es el separador en el archivo
    # también se puede utilizar quotechar='(carácter que envuelve una entrada)'
    # por ejemplo, una entrada en un archivo CSV podría ser "Hola;Mundo", que es igual al delimitador
    # eso significa que ahora hay que decirle a Python que el carácter " envuelve una entrada
    # se vería así: quotechar='"'
    for line in csv_file:
        print(line)
