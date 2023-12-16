# Inicializar variables
name_dictionary = {}
max_ocurrencias = 0
nombre_con_max_ocurrencias = ""

# Abrir el archivo CSV llamado "names.csv" en modo de lectura
with open("names.csv", "r") as archivo:
    # Iterar sobre cada línea en el archivo
    for linea in archivo:
        # Limpiar y dividir la línea por comas para obtener los datos
        datos = linea.strip().split(",")

        # Saltar la línea de encabezado
        if datos[0] == "id":
            continue

        # Obtener el nombre y la cantidad de ocurrencias desde los datos
        nombre = datos[1]
        cantidad = int(datos[2])

        # Actualizar el diccionario de nombres con la cantidad de ocurrencias
        if nombre in name_dictionary:
            name_dictionary[nombre] = name_dictionary[nombre] + cantidad
        else:
            name_dictionary[nombre] = cantidad

    # Encontrar el nombre con la mayor cantidad de ocurrencias
    for key, value in name_dictionary.items():
        if max_ocurrencias < value:
            max_ocurrencias = value
            nombre_con_max_ocurrencias = key

    # Imprimir el nombre con la mayor cantidad de ocurrencias y la cantidad de ocurrencias
    print(nombre_con_max_ocurrencias, max_ocurrencias)
    print(name_dictionary)
