# # Archivos
# # cómo abrir archivos de una manera que no se recomienda

# f = open("test.txt", "r")
# # se necesita especificar si se desea leer, escribir, agregar o leer y escribir
# # leer un archivo es r
# # escribir en un archivo es w
# # agregar a un archivo es a (se agregará al final del archivo)
# # leer y escribir es r+
# # crear un archivo usando x

# print(f.name)
# # 1)
# # .name imprimirá el nombre del archivo y NO su contenido
# # .mode imprimirá si el archivo está abierto para leer, escribir, etc.
# # .read() devolverá todo el texto / si deseas especificar, coloca un índice entre corchetes .read(5)
# # .readline() solo leerá una línea (comenzando desde la parte superior), si imprimes varias veces
# #    leerá la segunda, tercera, etc.
# # .readlines() devolverá cada línea en una lista
# #    puedes poner una pista entre corchetes para dar solo una cierta cantidad de caracteres

# # ¡si abrimos un archivo, necesitamos cerrarlo explícitamente!
# f.close()

# # para estar seguro, use un administrador de contexto para trabajar con archivos en Python
# # el administrador de contexto siempre cerrará el archivo por nosotros si trabajamos con uno; muy útil
# # f es una variable de objeto y tenemos acceso a ella, pero aún está cerrada
# # por eso tenemos que trabajar dentro del administrador de contexto
# with open("test.txt", "r") as f:
#     f_contents = f.read()  # ahora se pueden agregar funciones desde 1)
#     print(f_contents)

# # si tienes una línea en blanco en la consola, imprímela así: print(f_contents, end=" "
# #   end=" " eliminará la línea en blanco y siempre imprimirá la siguiente línea si la anterior termina

# # puedes iterar a través del archivo usando un bucle for, lo que lo hace más eficiente
# with open("test.txt", "r") as f:
#     for line in f:  # line es solo un nombre de variable, podría llamarse cualquier cosa
#         print(f_contents, end=" ")

# # .read(hint) especificación de cuántos caracteres leer
# with open("test.txt", "r") as f:
#     f_contents = f.read(100)  # lee 100 caracteres y luego se detiene
#     # se puede repetir varias veces hasta que el archivo no tenga más caracteres
#     f_contents = f.read(100)

# más control sobre lo que se va a leer
with open("test.txt", "r") as f:
    size_to_read = 100

    # poner en la variable f_contents los primeros 100 caracteres y leerlo
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end=" ")
        # línea muy importante aquí -> o de lo contrario, bucle infinito
        f_contents = f.read(size_to_read)
        # después de los primeros 100 caracteres, le decimos al bucle que tome el siguiente fragmento de 100 caracteres
        # si la variable tiene 0 caracteres (cadena vacía), entonces el bucle while terminará debido a las condiciones establecidas

with open("test.txt", "r") as f:
    size_to_read = 10

    f_contents = f.read(size_to_read)
    # nos dirá la posición en el archivo en la que estamos actualmente (en este caso, son 10)
    print(f.tell())

# ¿Cómo volver al principio del archivo?
# usa .seek()

with open("test.txt", "r") as f:
    size_to_read = 10

    f_contents = f.read(size_to_read)  # imprimirá los primeros 10 caracteres
    print(f_contents)
    f.seek(0)  # volverá a la posición 0
    # imprimirá nuevamente los primeros 10 caracteres del archivo
    f_contents = f.read(size_to_read)
    print(f_contents)

# CÓMO ESCRIBIR EN ARCHIVOS
# En caso de que el archivo aún no exista, creará automáticamente un nuevo archivo
with open("test.txt", "w") as f:
    f.write("Test")  # escribirá "Test" en el archivo
    # dato curioso
    f.seek(0)  # vuelve al índice 0
    # solo sobrescribiría la letra T, así que en el archivo será "Rest" ahora
    f.write("R")
    # o.. cuando se usa una palabra como "Sea", entonces en el archivo será "Seat"

# ¿Cómo recoger líneas de un archivo y escribirlas en otro?
# "r" solo en modo de lectura, variable con nombre rf para archivo de lectura
with open("test.txt", "r") as rf:
    # "w" en modo de escritura, variable con nombre wf para archivo de escritura
    with open("test_copy.txt", "w") as wf:
        for line in rf:  # para cada línea en nuestro archivo original, léela
            wf.write(line)  # y escríbela en el nuevo archivo

# Para trabajar con imágenes, necesitamos trabajar con modo binario
with open("test.jpg", "rb") as rf:  # se agregó b después de r para leer en modo binario
    # se agregó b después de w para escribir en modo binario
    with open("test_copy.jpg", "wb") as wf:
        for line in rf:
            # imprimirá cada línea de la imagen y la escribirá en el nuevo archivo .jpg
            wf.write(line)
            # el resultado será un archivo .jpg copiado

with open("test.jpg", "rb") as rf:
    with open("test_copy.jpg", "wb") as wf:
        chunk_size = 4096  # la cantidad de datos que queremos que el programa lea
        rf_chunk = rf.read(chunk_size)  # poner en 4096 en la variable rf_chunk y leerlo
        while len(rf_chunk) > 0:
